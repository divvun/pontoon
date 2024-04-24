# Generated by Django 2.2.11 on 2021-02-25 06:33

from django.db import migrations

from django.conf import settings

MIGRATION_0002_LOCALES = [
    {
        "code": "en",
        "google_translate_code": "en",
        "ms_translator_code": "",
        "ms_terminology_code": "en-us",
        "name": "English",
        "plural_rule": "(n != 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 1522576000,
    },
    {
        "code": "en-US",
        "google_translate_code": "en",
        "ms_translator_code": "",
        "ms_terminology_code": "en-us",
        "name": "English",
        "plural_rule": "(n != 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 308514000,
    },
    {
        "code": "fi",
        "google_translate_code": "fi",
        "ms_translator_code": "fi",
        "ms_terminology_code": "fi-fi",
        "name": "Finnish",
        "plural_rule": "(n != 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 5381000,
    },
    {
        "code": "fo",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "",
        "name": "Faroese",
        "plural_rule": "(n != 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 71000,
    },
    {
        "code": "is",
        "google_translate_code": "is",
        "ms_translator_code": "",
        "ms_terminology_code": "is-is",
        "name": "Icelandic",
        "plural_rule": "(n%10!=1 || n%100==11)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 332000,
    },
    {
        "code": "kl",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "",
        "name": "Kalaallisut",
        "plural_rule": "(n == 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 55000,
    },
    {
        "code": "nb",
        "google_translate_code": "no",
        "ms_translator_code": "",
        "ms_terminology_code": "nb-no",
        "name": "Norwegian Bokmål",
        "plural_rule": "(n != 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 5208000,
    },
    {
        "code": "nn",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "nn-no",
        "name": "Norwegian Nynorsk",
        "plural_rule": "(n != 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 1302000,
    },
    {
        "code": "se",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "",
        "name": "North Sámi",
        "plural_rule": "(n == 1 || n == 2)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 52000,
    },
    {
        "code": "sma",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "",
        "name": "South Sámi",
        "plural_rule": "(n == 1 || n == 2)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 800,
    },
    {
        "code": "smj",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "",
        "name": "Lule Sámi",
        "plural_rule": "(n == 1 || n == 2)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 4000,
    },
    {
        "code": "smn",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "",
        "name": "Inari Sámi",
        "plural_rule": "(n == 1 || n == 2)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 610,
    },
    {
        "code": "sms",
        "google_translate_code": "",
        "ms_translator_code": "",
        "ms_terminology_code": "",
        "name": "Skolt Sámi",
        "plural_rule": "(n == 1 || n == 2)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 610,
    },
    {
        "code": "sv-SE",
        "google_translate_code": "sv",
        "ms_translator_code": "",
        "ms_terminology_code": "sv-se",
        "name": "Swedish",
        "plural_rule": "(n != 1)",
        "cldr_plurals": "1,5",
        "script": "Latin",
        "direction": "ltr",
        "population": 9312000,
    },
]

MIGRATION_0146_USERS = [
    ("pontoon-tm@mozilla.com", "translation-memory", "Translation Memory"),
    ("pontoon-gt@mozilla.com", "google-translate", "Google Translate"),
]


def migration_0002_load_initial_data(apps, schema_editor):
    Locale = apps.get_model("base", "Locale")
    intro_locales = []
    for locale_kwargs in MIGRATION_0002_LOCALES:
        loc = Locale.objects.create(**locale_kwargs)
        if loc.code == "en-GB":
            intro_locales.append(loc)
    Project = apps.get_model("base", "Project")
    project = Project.objects.create(
        name="Pontoon Intro",
        slug="pontoon-intro",
        system_project=True,
        url=settings.SITE_URL + "/intro/",
        links=True,
        info="This is a demo website, used for demonstration purposes only. You can translate on the website itself by double clicking on page elements. Access to advanced features like translation memory and machine translation is available by clicking on the menu icon in the top-left corner.",
    )
    project.locales.set(intro_locales)
    Repository = apps.get_model("base", "Repository")
    Repository.objects.create(
        project=project,
        url="https://github.com/mozilla/pontoon-intro.git",
    )


def migration_0146_add_pretranslation_users(apps, schema_editor):
    User = apps.get_model("auth", "User")
    UserProfile = apps.get_model("base", "UserProfile")
    users = User.objects.bulk_create(
        [
            User(email=email, username=username, first_name=name)
            for email, username, name in MIGRATION_0146_USERS
        ]
    )
    UserProfile.objects.bulk_create([UserProfile(user=user) for user in users])


def migration_0041_create_locale_permissions(apps, schema_editor):
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model("contenttypes", "ContentType")
    locale_content_type, _ = ContentType.objects.get_or_create(
        app_label="base", model="locale"
    )
    Permission.objects.get_or_create(
        codename="can_translate_locale",
        content_type=locale_content_type,
        name="Can add translations",
    )
    Permission.objects.get_or_create(
        codename="can_manage_locale",
        content_type=locale_content_type,
        name="Can manage locale",
    )


def migration_0043_create_locale_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    Locale = apps.get_model("base", "Locale")
    ContentType = apps.get_model("contenttypes", "ContentType")
    GroupObjectPermission = apps.get_model("guardian", "GroupObjectPermission")
    locale_content_type = ContentType.objects.get(app_label="base", model="locale")
    can_translate = Permission.objects.get(
        content_type=locale_content_type, codename="can_translate_locale"
    )
    can_manage = Permission.objects.get(
        content_type=locale_content_type, codename="can_manage_locale"
    )
    for locale in Locale.objects.all():
        translators_group = Group.objects.create(name=f"{locale.code} translators")
        translators_group.permissions.add(can_translate)
        GroupObjectPermission.objects.create(
            object_pk=locale.pk,
            content_type=locale_content_type,
            group=translators_group,
            permission=can_translate,
        )
        managers_group = Group.objects.create(name=f"{locale.code} managers")
        managers_group.permissions.add(can_translate)
        GroupObjectPermission.objects.create(
            object_pk=locale.pk,
            content_type=locale_content_type,
            group=managers_group,
            permission=can_translate,
        )
        managers_group.permissions.add(can_manage)
        GroupObjectPermission.objects.create(
            object_pk=locale.pk,
            content_type=locale_content_type,
            group=managers_group,
            permission=can_manage,
        )
        locale.translators_group = translators_group
        locale.managers_group = managers_group
        locale.save()


def squashed_run_python(apps, schema_editor):
    migration_0002_load_initial_data(apps, schema_editor)
    migration_0041_create_locale_permissions(apps, schema_editor)
    migration_0043_create_locale_groups(apps, schema_editor)
    migration_0146_add_pretranslation_users(apps, schema_editor)


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_squashed_0154_auto_20200206_1736"),
        ("guardian", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [migrations.RunPython(squashed_run_python)]
