from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_type', models.IntegerField(choices=[(0, 'Assets'), (1, 'Capital'), (2, 'Liabilities'), (3, 'Revenue'), (4, 'Expenses')])),
                ('name', models.CharField(help_text='Name of this ledger', max_length=256)),
                ('description', models.TextField(blank=True, help_text='Any notes to go along with this Transaction.')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.IntegerField(choices=[(0, 'Manual'), (1, 'Automated')])),
                ('notes', models.TextField(blank=True, help_text='Any notes to go along with this Transaction.')),
                ('posted_timestamp', models.DateTimeField(db_index=True, help_text='Time the transaction was posted. Change this field to model retroactive ledger entries.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voids', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voided_by', to='simple_accounting.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionEvidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.IntegerField(choices=[(0, 'Order')])),
                ('object_id', models.IntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidences', to='simple_accounting.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='LedgerEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.PositiveIntegerField(blank=True, null=True)),
                ('credit', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='simple_accounting.ledger')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='simple_accounting.transaction')),
            ],
        ),
    ]