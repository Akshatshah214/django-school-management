# Generated by Django 4.1.2 on 2022-10-17 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MBloodGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("delete_status", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "m_blood_group",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="MClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=2)),
                ("delete_status", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "m_class",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="MGender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("delete_status", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "m_gender",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="MInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateTimeField()),
                ("address", models.CharField(max_length=255)),
                ("mobile_number", models.IntegerField(null=True)),
                ("fathers_name", models.CharField(max_length=100)),
                ("fathers_number", models.IntegerField()),
                ("mothers_name", models.CharField(max_length=100)),
                ("mothers_number", models.IntegerField()),
                ("delete_status", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "m_info",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="MStandardClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("standard", models.SmallIntegerField()),
                ("delete_status", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "m_standard_class",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="MSubject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("delete_status", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "m_subject",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="TTeacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("activate", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="school.minfo",
                    ),
                ),
                (
                    "standard_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="school.mstandardclass",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="school.msubject",
                    ),
                ),
            ],
            options={
                "db_table": "t_teacher",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="TStudent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("activate", models.BooleanField(blank=True, null=True)),
                ("created_user_id", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_user_id", models.CharField(max_length=100)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                (
                    "info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="school.minfo",
                    ),
                ),
                (
                    "standard_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="school.mstandardclass",
                    ),
                ),
            ],
            options={
                "db_table": "t_student",
                "managed": True,
            },
        ),
        migrations.AddIndex(
            model_name="msubject",
            index=models.Index(fields=["id"], name="m_subject_index"),
        ),
        migrations.AddField(
            model_name="mstandardclass",
            name="standard_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="school.mclass"
            ),
        ),
        migrations.AddField(
            model_name="minfo",
            name="blood_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="school.mbloodgroup"
            ),
        ),
        migrations.AddField(
            model_name="minfo",
            name="gender",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="school.mgender"
            ),
        ),
        migrations.AddIndex(
            model_name="mgender",
            index=models.Index(fields=["id"], name="m_gender_index"),
        ),
        migrations.AddIndex(
            model_name="mclass",
            index=models.Index(fields=["id"], name="m_class_index"),
        ),
        migrations.AddIndex(
            model_name="mbloodgroup",
            index=models.Index(fields=["id"], name="m_blood_group_index"),
        ),
        migrations.AddIndex(
            model_name="tteacher",
            index=models.Index(fields=["id"], name="t_teacher_index"),
        ),
        migrations.AddIndex(
            model_name="tstudent",
            index=models.Index(fields=["id"], name="t_student_index"),
        ),
        migrations.AddIndex(
            model_name="mstandardclass",
            index=models.Index(fields=["id"], name="m_standard_class_index"),
        ),
        migrations.AddIndex(
            model_name="minfo",
            index=models.Index(fields=["id"], name="m_info_index"),
        ),
    ]
