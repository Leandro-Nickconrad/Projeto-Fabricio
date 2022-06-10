from django import forms


class FormCadastrar(forms.Form):

    titulo = forms.CharField(label='Título', widget=forms.TextInput())
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea())
    nome_da_imagem = forms.CharField(label='Nome da Imagem', widget=forms.TextInput())
    duracao = forms.CharField(label='Duração', widget=forms.TextInput())
    producao = forms.CharField(label='Produção', widget=forms.TextInput())
    direcao = forms.CharField(label='Direção', widget=forms.TextInput())
    esta_em_cartaz = forms.BooleanField(required=False)

class FormPesquisar(forms.Form):

    pesquisar = forms.CharField(label='Pesquisar', widget=forms.TextInput(attrs={'class':'form-control me-2', 'placeholder': 'Pesquisar Filme'}))