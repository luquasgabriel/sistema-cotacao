from datetime import time

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.access.models import ClassSchedule, Room, Teacher


ROOMS = [
    {
        "name": "Lab. 1-08",
        "code": "LAB-1-08",
        "location": "Bloco 1",
        "capacity": 0,
    },
    {
        "name": "Lab. 1-09",
        "code": "LAB-1-09",
        "location": "Bloco 1",
        "capacity": 0,
    },
    {
        "name": "Lab. 1-10",
        "code": "LAB-1-10",
        "location": "Bloco 1",
        "capacity": 0,
    },
    {
        "name": "Lab. CAD 3",
        "code": "LAB-CAD-3",
        "location": "CAD",
        "capacity": 0,
    },
]

TEACHERS = [
    {
        "username": "ivo.augusto",
        "email": "ivo.augusto@ifal.edu.br",
        "first_name": "Ivo",
        "last_name": "Augusto",
        "employee_number": "PROF-IVO-AUGUSTO",
    },
    {
        "username": "anderson.rodrigues",
        "email": "anderson.rodrigues@ifal.edu.br",
        "first_name": "Anderson",
        "last_name": "Rodrigues",
        "employee_number": "PROF-ANDERSON-RODRIGUES",
    },
    {
        "username": "elvys.alves",
        "email": "elvys.alves@ifal.edu.br",
        "first_name": "Elvys",
        "last_name": "Alves",
        "employee_number": "PROF-ELVYS-ALVES",
    },
    {
        "username": "edison.camilo",
        "email": "edison.camilo@ifal.edu.br",
        "first_name": "Edison",
        "last_name": "Camilo",
        "employee_number": "PROF-EDISON-CAMILO",
    },
    {
        "username": "jose.simplicio.neto",
        "email": "jose.simplicio.neto@ifal.edu.br",
        "first_name": "José Simplício",
        "last_name": "Neto",
        "employee_number": "PROF-JOSE-SIMPLICIO-NETO",
    },
    {
        "username": "wellington",
        "email": "wellington@ifal.edu.br",
        "first_name": "Wellington",
        "last_name": "",
        "employee_number": "PROF-WELLINGTON",
    },
]

SCHEDULES = [
    {
        "teacher": "ivo.augusto",
        "room": "LAB-1-09",
        "subject": "Eletiva",
        "weekday": ClassSchedule.Weekday.MONDAY,
        "starts_at": time(18, 50),
        "ends_at": time(20, 30),
    },
    {
        "teacher": "anderson.rodrigues",
        "room": "LAB-CAD-3",
        "subject": "Empreendedorismo Digital",
        "weekday": ClassSchedule.Weekday.MONDAY,
        "starts_at": time(20, 40),
        "ends_at": time(22, 20),
    },
    {
        "teacher": "ivo.augusto",
        "room": "LAB-1-09",
        "subject": "Eletiva",
        "weekday": ClassSchedule.Weekday.TUESDAY,
        "starts_at": time(18, 50),
        "ends_at": time(20, 30),
    },
    {
        "teacher": "elvys.alves",
        "room": "LAB-1-10",
        "subject": "Processos de Desenvolvimentos de Software",
        "weekday": ClassSchedule.Weekday.TUESDAY,
        "starts_at": time(20, 40),
        "ends_at": time(22, 20),
    },
    {
        "teacher": "edison.camilo",
        "room": "LAB-1-10",
        "subject": "Projeto Integrador em Sistema de Informação",
        "weekday": ClassSchedule.Weekday.WEDNESDAY,
        "starts_at": time(18, 50),
        "ends_at": time(20, 30),
    },
    {
        "teacher": "edison.camilo",
        "room": "LAB-1-10",
        "subject": "Projeto Integrador em Sistema de Informação",
        "weekday": ClassSchedule.Weekday.WEDNESDAY,
        "starts_at": time(20, 40),
        "ends_at": time(22, 20),
    },
    {
        "teacher": "elvys.alves",
        "room": "LAB-1-10",
        "subject": "Processos de Desenvolvimentos de Software",
        "weekday": ClassSchedule.Weekday.THURSDAY,
        "starts_at": time(18, 50),
        "ends_at": time(20, 30),
    },
    {
        "teacher": "anderson.rodrigues",
        "room": "LAB-CAD-3",
        "subject": "Empreendedorismo Digital",
        "weekday": ClassSchedule.Weekday.THURSDAY,
        "starts_at": time(20, 40),
        "ends_at": time(22, 20),
    },
    {
        "teacher": "jose.simplicio.neto",
        "room": "LAB-1-10",
        "subject": "Laboratório de Sistemas Operacionais e Redes",
        "weekday": ClassSchedule.Weekday.FRIDAY,
        "starts_at": time(18, 50),
        "ends_at": time(20, 30),
    },
    {
        "teacher": "wellington",
        "room": "LAB-1-08",
        "subject": "Computação Forense",
        "weekday": ClassSchedule.Weekday.FRIDAY,
        "starts_at": time(20, 40),
        "ends_at": time(22, 20),
    },
]


class Command(BaseCommand):
    help = "Preenche o banco com salas, professores e horarios de aula informados."

    def add_arguments(self, parser):
        parser.add_argument(
            "--class-group",
            default="Turma noturna",
            help="Turma usada nos horarios criados ou atualizados.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Mostra a quantidade de registros planejados sem alterar o banco.",
        )

    def handle(self, *args, **options):
        class_group = options["class_group"]

        if options["dry_run"]:
            self.stdout.write(
                "Carga simulada: "
                f"{len(ROOMS)} salas, {len(TEACHERS)} professores e "
                f"{len(SCHEDULES)} horarios seriam processados."
            )
            return

        with transaction.atomic():
            room_results = self._seed_rooms()
            teacher_results = self._seed_teachers()
            schedule_results = self._seed_schedules(
                room_results["objects"],
                teacher_results["objects"],
                class_group,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Carga concluida: "
                f"{self._format_result(room_results, 'sala')}, "
                f"{self._format_result(teacher_results, 'professor')}, "
                f"{self._format_result(schedule_results, 'horario')}."
            )
        )

    def _seed_rooms(self):
        results = self._empty_results()

        for room_data in ROOMS:
            room, created = Room.objects.get_or_create(
                code=room_data["code"],
                defaults={
                    "name": room_data["name"],
                    "location": room_data["location"],
                    "capacity": room_data["capacity"],
                    "status": Room.Status.AVAILABLE,
                },
            )
            if not created:
                self._update_fields(
                    room,
                    {
                        "name": room_data["name"],
                        "location": room_data["location"],
                        "capacity": room_data["capacity"],
                    },
                )

            self._count_result(results, created)
            results["objects"][room.code] = room

        return results

    def _seed_teachers(self):
        results = self._empty_results()
        user_model = get_user_model()

        for teacher_data in TEACHERS:
            self._validate_user_email(user_model, teacher_data)

            user, user_created = user_model.objects.get_or_create(
                username=teacher_data["username"],
                defaults={
                    "email": teacher_data["email"],
                    "first_name": teacher_data["first_name"],
                    "last_name": teacher_data["last_name"],
                    "is_active": True,
                },
            )

            if user_created:
                user.set_unusable_password()
                user.save(update_fields=["password"])
            else:
                self._update_fields(
                    user,
                    {
                        "email": teacher_data["email"],
                        "first_name": teacher_data["first_name"],
                        "last_name": teacher_data["last_name"],
                    },
                )

            self._validate_employee_number(user, teacher_data)

            teacher, teacher_created = Teacher.objects.get_or_create(
                user=user,
                defaults={
                    "employee_number": teacher_data["employee_number"],
                    "is_active": True,
                },
            )
            if not teacher_created:
                self._update_fields(
                    teacher,
                    {
                        "employee_number": teacher_data["employee_number"],
                        "is_active": True,
                    },
                )

            self._count_result(results, user_created or teacher_created)
            results["objects"][teacher_data["username"]] = teacher

        return results

    def _seed_schedules(self, rooms, teachers, class_group):
        results = self._empty_results()

        for schedule_data in SCHEDULES:
            schedule, created = ClassSchedule.objects.update_or_create(
                teacher=teachers[schedule_data["teacher"]],
                room=rooms[schedule_data["room"]],
                subject=schedule_data["subject"],
                weekday=schedule_data["weekday"],
                starts_at=schedule_data["starts_at"],
                ends_at=schedule_data["ends_at"],
                defaults={
                    "class_group": class_group,
                    "is_active": True,
                },
            )
            self._count_result(results, created)
            results["objects"][schedule.pk] = schedule

        return results

    def _validate_user_email(self, user_model, teacher_data):
        conflicting_user = (
            user_model.objects.filter(email=teacher_data["email"])
            .exclude(username=teacher_data["username"])
            .first()
        )
        if conflicting_user:
            raise CommandError(
                f"O email {teacher_data['email']} ja esta em uso pelo usuario "
                f"{conflicting_user.username}."
            )

    def _validate_employee_number(self, user, teacher_data):
        conflicting_teacher = (
            Teacher.objects.filter(employee_number=teacher_data["employee_number"])
            .exclude(user=user)
            .first()
        )
        if conflicting_teacher:
            raise CommandError(
                "A matricula funcional "
                f"{teacher_data['employee_number']} ja esta em uso por "
                f"{conflicting_teacher}."
            )

    def _update_fields(self, instance, values):
        changed_fields = []

        for field, value in values.items():
            if getattr(instance, field) != value:
                setattr(instance, field, value)
                changed_fields.append(field)

        if changed_fields:
            instance.save(update_fields=changed_fields)

    def _empty_results(self):
        return {
            "created": 0,
            "updated": 0,
            "objects": {},
        }

    def _count_result(self, results, created):
        if created:
            results["created"] += 1
        else:
            results["updated"] += 1

    def _format_result(self, results, singular_name):
        total = results["created"] + results["updated"]
        return (
            f"{total} {singular_name}(s) "
            f"({results['created']} criado(s), {results['updated']} atualizado(s))"
        )
