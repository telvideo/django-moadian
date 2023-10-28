# Generated by Django 4.2.6 on 2023-10-25 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'صورتحساب',
                'verbose_name_plural': 'صورتحساب ها',
            },
        ),
        migrations.CreateModel(
            name='InvoiceResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(blank=True, null=True)),
                ('reference_number', models.UUIDField(blank=True, null=True)),
                ('error_code', models.PositiveIntegerField(blank=True, null=True)),
                ('error_detail', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('confirmation_reference_id', models.UUIDField(blank=True, null=True)),
                ('errors', models.TextField(blank=True, null=True)),
                ('warnings', models.TextField(blank=True, null=True)),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
            ],
            options={
                'verbose_name': 'InvoiceResult',
                'verbose_name_plural': 'InvoiceResults',
            },
        ),
        migrations.CreateModel(
            name='InvoicePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iinn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره سوییچ پرداخت')),
                ('acn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره پذیرنده فروشگاهی')),
                ('trmn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره پایانه')),
                ('trn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره پیگیری')),
                ('pcn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره کارت پرداخت کننده صورتحساب')),
                ('pid', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره/شناسه ملی/کد فراگیر اتباع غیر ایرانی پرداخت کننده صورتحساب')),
                ('pdt', models.DateTimeField(blank=True, max_length=50, null=True, verbose_name='تاریخ و زمان پرداخت صورتحساب')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
            ],
            options={
                'verbose_name': 'InvoicePayment',
                'verbose_name_plural': 'InvoicePayments',
            },
        ),
        migrations.CreateModel(
            name='InvoiceHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxid', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره منحصر به فرد مالیاتی')),
                ('indatim', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ صدور صورتحساب')),
                ('indati2m', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ ایجاد صورتحساب')),
                ('inty', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'نوع اول'), (2, 'نوع دوم'), (3, 'نوع سوم')], default=1, null=True, verbose_name='نوع صورتحساب')),
                ('inno', models.CharField(blank=True, max_length=50, null=True, verbose_name='سریال صورتحساب')),
                ('irtaxid', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره منحصر به فرد سریال صورتحساب مرجع')),
                ('inp', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'فروش'), (2, 'فروش ارزی'), (3, 'طلا و جواهر و پلاتین'), (4, 'قرارداد پیمانکاری'), (5, 'قبوض خدماتی'), (6, 'بلیت هواپیما')], default=1, null=True, verbose_name='الگوی صورتحساب')),
                ('ins', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'اصلی'), (2, 'اصلاحی'), (3, 'ابطالی'), (4, 'برگشت از فروش')], default=1, null=True, verbose_name='موضوع صورتحساب')),
                ('tins', models.CharField(blank=True, default='10101704295', max_length=15, null=True, verbose_name='شماره اقتصادی فروشنده')),
                ('tinb', models.CharField(blank=True, max_length=15, null=True, verbose_name='شماره اقتصادی خریدار')),
                ('tob', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'حقیقی'), (2, 'حقوقی'), (3, 'مشارکت مدنی'), (4, 'اتباع غیرایرانی'), (5, 'مصرف کننده نهایی')], default=2, null=True, verbose_name='نوع شخص خریدار')),
                ('bid', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره/شناسه ملی/شناسه مشارکت مدنی/کد فراگیر خریدار')),
                ('sbc', models.CharField(blank=True, max_length=15, null=True, verbose_name='کد شعبه فروشنده')),
                ('bpc', models.CharField(blank=True, max_length=15, null=True, verbose_name='کد پستی خریدار')),
                ('bbc', models.CharField(blank=True, max_length=15, null=True, verbose_name='کد شعبه خریدار')),
                ('ft', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='نوع پرواز')),
                ('bpn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره گذرنامه خریدار')),
                ('scln', models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره پروانه گمرکی')),
                ('scc', models.CharField(blank=True, max_length=50, null=True, verbose_name='کد گمرک محل اظهار')),
                ('crn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شناسه یکتای ثبت قرارداد فروشنده')),
                ('billid', models.CharField(blank=True, max_length=50, null=True, verbose_name='شناسه اشتراک/شماره قبض بهره بردار')),
                ('tprdis', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مجموع مبلغ قبل از کسر تخفیف')),
                ('tdis', models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='مجموع تخفیفات')),
                ('tadis', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مجموع مبلغ پس از کسر تخفیف')),
                ('tvam', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مجموع مالیات بر ارزش افزوده')),
                ('todam', models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='مجموع سایر مالیات، عوارض و وجوه قانونی')),
                ('tbill', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مجموع صورتحساب')),
                ('setm', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'نقدی'), (2, 'نسیه'), (3, 'نقدی/نسیه')], default=1, null=True, verbose_name='روش تسویه')),
                ('cap', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ پرداختی نقدی')),
                ('insp', models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='مبلغ پرداختی نسیه')),
                ('tvop', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مجموع سهم مالیات بر ارزش افزوده از پرداخت')),
                ('tax17', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مالیات موضوع ماده ۱۷')),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
            ],
            options={
                'verbose_name': 'InvoiceHeader',
                'verbose_name_plural': 'InvoiceHeaders',
            },
        ),
        migrations.CreateModel(
            name='InvoiceBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sstid', models.CharField(blank=True, max_length=50, null=True, verbose_name='شناسه کالا/خدمت')),
                ('sstt', models.CharField(blank=True, max_length=50, null=True, verbose_name='شرح کالا/خدمت')),
                ('am', models.PositiveIntegerField(blank=True, null=True, verbose_name='تعداد/مقدار کالا')),
                ('mu', models.CharField(blank=True, max_length=4, null=True, verbose_name='واحد اندازه گیزی')),
                ('fee', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ واحد')),
                ('cfee', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='میزان ارز')),
                ('cut', models.CharField(blank=True, max_length=50, null=True, verbose_name='نوع ارز')),
                ('exr', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='نرخ برابری ارز با ریال')),
                ('prdis', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ قبل از تخفیف')),
                ('dis', models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='مبلغ تخفیف')),
                ('adis', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ بعد از تخفیف')),
                ('vra', models.PositiveBigIntegerField(blank=True, default=9, null=True, verbose_name='نرخ مالیات بر ارزش افزوده')),
                ('vam', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ مالیات بر ارزش افزوده')),
                ('odt', models.CharField(blank=True, max_length=50, null=True, verbose_name='موضوع سایر مالیات و عوارض')),
                ('odr', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='نرخ سایر مالیات و عوارض')),
                ('odam', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ سایر مالیات و عوارض')),
                ('olt', models.CharField(blank=True, max_length=50, null=True, verbose_name='موضوع سایر وجوه قانونی')),
                ('olr', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='نرخ سایر وجوه قانونی')),
                ('olam', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ سایر وجوه قانونی')),
                ('consfee', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='اجرت ساخت')),
                ('spro', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='سود فروشنده')),
                ('bros', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='حق العمل')),
                ('tcpbs', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='جمع کل اجرت، حق العمل و سود فروشنده')),
                ('cop', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='سهم نقدی از پرداخت')),
                ('vop', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='سهم ارزش افزوده از پرداخت')),
                ('bsrn', models.CharField(blank=True, max_length=50, null=True, verbose_name='شناسه یکتای ثبت قرارداد حق العملکاری')),
                ('tsstam', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='مبلغ کل کالا/خدمت')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
            ],
            options={
                'verbose_name': 'InvoiceBody',
                'verbose_name_plural': 'InvoiceBodys',
            },
        ),
    ]
