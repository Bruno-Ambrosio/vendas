# Generated by Django 4.2.6 on 2023-11-15 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_rename_fornecedor_celular_fornecedores_fornecedor_contato_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_cep',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_complemento',
            new_name='complemento',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_contato',
            new_name='contato',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_cpf',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_endereco',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_numero',
            new_name='numero',
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='cliente_rg',
            new_name='rg',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_cep',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_cnpj',
            new_name='cnpj',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_complemento',
            new_name='complemento',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_contato',
            new_name='contato',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_endereco',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_numero',
            new_name='numero',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_cargo',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_cep',
            new_name='cep',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_complemento',
            new_name='complemento',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_contato',
            new_name='contato',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_cpf',
            new_name='cpf',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_endereco',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_estado',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_nivel_acesso',
            new_name='nivel_acesso',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_nome',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_numero',
            new_name='numero',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_rg',
            new_name='rg',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_senha',
            new_name='senha',
        ),
        migrations.RenameField(
            model_name='produtos',
            old_name='produto_descricao',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='vendas',
            old_name='data_venda',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='vendas',
            old_name='total_venda',
            new_name='total',
        ),
    ]
