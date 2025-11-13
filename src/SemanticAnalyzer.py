from QuizLangVisitor import QuizLangVisitor
from QuizLangParser import QuizLangParser

class Symbol:
    def __init__(self, name, type, scope=None):
        self.name = name
        self.type = type
        self.scope = scope

class SymbolTable:
    def __init__(self):
        self.symbols = {}  # (scope, name) -> Symbol
        self.scope_stack = ['global']
        self.current_scope = 'global'
        self.tasks = []
        self.connections = {}
        self.variables = {}  # scope -> {name: type}

    def enter_scope(self, scope_name):
        self.scope_stack.append(scope_name)
        self.current_scope = scope_name
        if scope_name not in self.connections:
            self.connections[scope_name] = []
        if scope_name not in self.variables:
            self.variables[scope_name] = {}

    def exit_scope(self):
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()
        self.current_scope = self.scope_stack[-1]

    def define(self, name, type, scope=None):
        if scope is None:
            scope = self.current_scope
        key = (scope, name)
        if key in self.symbols:
            return False  # Symbol already exists in this scope
        sym = Symbol(name, type, scope)
        self.symbols[key] = sym
        self.variables.setdefault(scope, {})[name] = type
        return True

    def lookup(self, name):
        # Search from the current scope up to global
        for s in reversed(self.scope_stack):
            key = (s, name)
            if key in self.symbols:
                return self.symbols[key]
        return None

    def get_all_symbols(self):
        return list(self.symbols.values())

    def get_variables(self):
        return self.variables

class SemanticAnalyzer(QuizLangVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def visitQuiz(self, ctx:QuizLangParser.QuizContext):
        quiz_id = ctx.ID().getText()
        self.symbol_table.enter_scope(quiz_id)
        # Quiz é uma variável do tipo 'quiz' no escopo global
        if not self.symbol_table.define(quiz_id, 'quiz', 'global'):
            self.errors.append(f"Erro: O quiz com ID '{quiz_id}' já foi definido no escopo global.")
        result = self.visitChildren(ctx)
        self.symbol_table.exit_scope()
        return result

    def visitMetadados(self, ctx:QuizLangParser.MetadadosContext):
        # Titulo e tempo são variáveis do quiz
        titulo = ctx.STRING().getText().strip('"')
        tempo = ctx.NUMBER().getText()
        quiz_scope = self.symbol_table.current_scope
        # Titulo: string
        if not self.symbol_table.define('titulo', 'string', quiz_scope):
            self.errors.append(f"Erro: Variável 'titulo' já definida no escopo '{quiz_scope}'.")
        # Tempo: número
        if not self.symbol_table.define('tempo', 'number', quiz_scope):
            self.errors.append(f"Erro: Variável 'tempo' já definida no escopo '{quiz_scope}'.")
        return self.visitChildren(ctx)

    def visitSecao(self, ctx:QuizLangParser.SecaoContext):
        raw_name = ctx.STRING().getText()
        section_name = raw_name.strip('"')
        self.symbol_table.enter_scope(section_name)
        # Seção é uma variável do tipo 'secao' no escopo do quiz
        quiz_scope = self.symbol_table.scope_stack[-2] if len(self.symbol_table.scope_stack) > 1 else 'global'
        if not self.symbol_table.define(section_name, 'secao', quiz_scope):
            self.errors.append(f"Erro: A seção '{section_name}' já foi definida no escopo '{quiz_scope}'.")
        result = self.visitChildren(ctx)
        if not self.symbol_table.variables.get(section_name):
            self.errors.append(f"Aviso: A seção '{section_name}' não contém questões.")
        self.symbol_table.exit_scope()
        return result

    def visitMcq(self, ctx:QuizLangParser.McqContext):
        question_id = ctx.ID().getText()
        # MCQ é uma variável do tipo 'mcq' no escopo da seção
        section_scope = self.symbol_table.current_scope
        if not self.symbol_table.define(question_id, 'mcq', section_scope):
            self.errors.append(f"Erro: A questão com ID '{question_id}' já foi definida no escopo '{section_scope}'.")
        else:
            # Adiciona a questão à lista de conexões da seção
            self.symbol_table.connections.setdefault(section_scope, []).append(question_id)

        opcoes = [opt.getText() for opt in ctx.opcoes().STRING()]
        resposta = ctx.STRING().getText()
        opcoes_sem_aspas = [opt.strip('"') for opt in opcoes]
        resposta_sem_aspas = resposta.strip('"')
        # Opções: lista de string
        if not self.symbol_table.define(f"{question_id}_opcoes", 'list<string>', section_scope):
            self.errors.append(f"Erro: Variável de opções para '{question_id}' já definida no escopo '{section_scope}'.")
        # Resposta: string
        if not self.symbol_table.define(f"{question_id}_resposta", 'string', section_scope):
            self.errors.append(f"Erro: Variável de resposta para '{question_id}' já definida no escopo '{section_scope}'.")
        if len(opcoes_sem_aspas) < 2:
            self.errors.append(f"Erro: A questão '{question_id}' deve ter pelo menos duas opções.")
        if len(set(opcoes_sem_aspas)) != len(opcoes_sem_aspas):
            self.errors.append(f"Erro: A questão '{question_id}' possui opções duplicadas.")
        if resposta_sem_aspas not in opcoes_sem_aspas:
            self.errors.append(f"Erro: A resposta '{resposta_sem_aspas}' para a questão '{question_id}' não é uma das opções válidas.")
        return self.visitChildren(ctx)

    def visitDiscursiva(self, ctx:QuizLangParser.DiscursivaContext):
        question_id = ctx.ID().getText()
        section_scope = self.symbol_table.current_scope
        if not self.symbol_table.define(question_id, 'discursiva', section_scope):
            self.errors.append(f"Erro: A questão com ID '{question_id}' já foi definida no escopo '{section_scope}'.")
        else:
            # Adiciona a questão à lista de conexões da seção
            self.symbol_table.connections.setdefault(section_scope, []).append(question_id)

        # Limite de palavras: number
        if not self.symbol_table.define(f"{question_id}_palavras", 'number', section_scope):
            self.errors.append(f"Erro: Variável de palavras para '{question_id}' já definida no escopo '{section_scope}'.")
        try:
            number_token = ctx.NUMBER().getText()
            num = int(number_token)
            if num <= 0:
                self.errors.append(f"Erro: Número de palavras para a questão '{question_id}' deve ser maior que zero.")
        except Exception:
            nums = [n.getText() for n in ctx.NUMBER()]
            if nums:
                try:
                    if int(nums[0]) <= 0:
                        self.errors.append(f"Erro: Número de palavras para a questão '{question_id}' deve ser maior que zero.")
                except ValueError:
                    self.errors.append(f"Erro: Número inválido para palavras na questão '{question_id}'.")
        return self.visitChildren(ctx)

    def visitNumerica(self, ctx:QuizLangParser.NumericaContext):
        question_id = ctx.ID().getText()
        section_scope = self.symbol_table.current_scope
        if not self.symbol_table.define(question_id, 'numerica', section_scope):
            self.errors.append(f"Erro: A questão com ID '{question_id}' já foi definida no escopo '{section_scope}'.")
        else:
            # Adiciona a questão à lista de conexões da seção
            self.symbol_table.connections.setdefault(section_scope, []).append(question_id)

        # Intervalo: dois números
        if not self.symbol_table.define(f"{question_id}_intervalo", 'tuple<number,number>', section_scope):
            self.errors.append(f"Erro: Variável de intervalo para '{question_id}' já definida no escopo '{section_scope}'.")
        nums = [n.getText() for n in ctx.NUMBER()]
        if len(nums) >= 2:
            try:
                a = int(nums[0])
                b = int(nums[1])
                if a > b:
                    self.errors.append(f"Erro: Intervalo inválido na questão '{question_id}': {a} > {b}.")
            except ValueError:
                self.errors.append(f"Erro: Valores não-inteiros no intervalo da questão '{question_id}'.")
        else:
            self.errors.append(f"Erro: Intervalo incompleto na questão '{question_id}'.")
        return self.visitChildren(ctx)

    def report(self):
        lines = []
        lines.append('--- Relatório Semântico ---')
        lines.append('\nVariáveis, tipos e escopos:')
        for scope, vars in self.symbol_table.get_variables().items():
            lines.append(f"Escopo '{scope}':")
            for name, typ in vars.items():
                lines.append(f"  - {name}: {typ}")
        lines.append('\nSímbolos registrados:')
        for sym in self.symbol_table.get_all_symbols():
            lines.append(f"- {sym.type} '{sym.name}' (escopo: {sym.scope})")
        lines.append('\nConexões (seção -> questões):')
        for scope, names in self.symbol_table.connections.items():
            lines.append(f"- {scope}: {', '.join(names) if names else '(nenhuma)'}")
        lines.append('\nErros e avisos:')
        if self.errors:
            for e in self.errors:
                lines.append(f"- {e}")
        else:
            lines.append('- Nenhum erro semântico detectado')
        return '\n'.join(lines)