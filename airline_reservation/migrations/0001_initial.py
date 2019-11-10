# Generated by Django 2.2.4 on 2019-09-15 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_end', models.CharField(choices=[('김포(GMP) - 부산(PUS)', '김포(GMP) - 부산(PUS)'), ('김포(GMP) - 제주(CJU)', '김포(GMP) - 제주(CJU)'), ('부산(PUS) - 제주(CJU)', '부산(PUS) - 제주(CJU)'), ('부산(PUS) - 김포(GMP)', '부산(PUS) - 김포(GMP)'), ('제주(CJU) - 김포(GMP)', '제주(CJU) - 김포(GMP)'), ('제주(CJU) - 부산(PUS)', '제주(CJU) - 부산(PUS)')], max_length=200)),
                ('passenger_name', models.CharField(max_length=200)),
                ('passenger_classification_adult', models.IntegerField()),
                ('passenger_classification_infant', models.IntegerField()),
                ('passenger_classification_child', models.IntegerField()),
                ('contect', models.CharField(max_length=200)),
                ('ticket_number', models.IntegerField()),
                ('reservation_number', models.IntegerField()),
                ('seat_level', models.CharField(choices=[('일반석', '일반석'), ('프레스티지석', '프레스티지석')], max_length=100)),
                ('one_or_round', models.CharField(choices=[('편도', '편도'), ('왕복', '왕복')], max_length=100)),
                ('fine_day', models.DateTimeField(verbose_name='(Fine)가는날')),
                ('comming_day', models.DateTimeField(verbose_name='(Comm)오는날')),
                ('flight_name', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField(auto_now=True)),
                ('arrival_time', models.DateTimeField(auto_now=True)),
                ('member_table', models.CharField(choices=[('스카이패스회원', '스카이패스회원'), ('비회원', '비회원')], max_length=100)),
                ('price', models.IntegerField()),
                ('passenger_number', models.IntegerField()),
                ('ticket_reservation_date', models.DateTimeField(auto_now_add=True)),
                ('flight_time', models.CharField(max_length=200)),
                ('luggage', models.IntegerField()),
                ('method_of_payment', models.CharField(choices=[('신용카드', '신용카드'), ('실시간걔좌이체', '실시간걔좌이체'), ('카카오페이', '카카오페이')], max_length=100)),
                ('payment', models.IntegerField()),
                ('billing_number', models.IntegerField()),
            ],
        ),
    ]
