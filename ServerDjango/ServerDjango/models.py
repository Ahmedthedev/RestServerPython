from django.db import models


class Professor(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    fk_professor_subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )

class Subject(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

class Classe(models.Model):
    date = models.DateTimeField()
    duration = models.IntegerField()
    fk_classe_subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )

class Promotion(models.Model):
        code = models.CharField(max_length=5)
        duration = models.CharField(max_length=50)
        fk_promotion_classe = models.ForeignKey(
            'Classe',
            on_delete=models.CASCADE,
        )

class SubjectPromotionFk(models.Model):
    fk_subjectpromotionfk_subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )
    fk_subjectpromotionfk_promotion = models.ForeignKey(
        'Promotion',
        on_delete=models.CASCADE,
    )


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    fk_student_classe = models.ForeignKey(
        'Classe',
        on_delete=models.CASCADE,
    )

