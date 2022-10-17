from django.db import models
from school.utils.utils import Utils


class MBloodGroup(models.Model):
    name = models.CharField(max_length=100)
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(MBloodGroup, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        indexes = [
            models.Index(
                name="m_blood_group_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "m_blood_group"


class MGender(models.Model):
    name = models.CharField(max_length=10)
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(MGender, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        indexes = [
            models.Index(
                name="m_gender_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "m_gender"


class MClass(models.Model):
    name = models.CharField(max_length=2)
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(MClass, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        indexes = [
            models.Index(
                name="m_class_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "m_class"


class TStandardClass(models.Model):
    standard = models.SmallIntegerField()
    standard_class = models.ForeignKey(MClass, models.DO_NOTHING)
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(TStandardClass, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.standard) + "_" + str(self.standard_class)

    class Meta:
        indexes = [
            models.Index(
                name="t_standard_class_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "t_standard_class"


class MSubject(models.Model):
    name = models.CharField(max_length=100)
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(MSubject, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        indexes = [
            models.Index(
                name="m_subject_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "m_subject"


class TPersonData(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=255)
    gender = models.ForeignKey(MGender, models.DO_NOTHING)
    blood_group = models.ForeignKey(MBloodGroup, models.DO_NOTHING)
    mobile_number = models.IntegerField(null=True)
    fathers_name = models.CharField(max_length=100)
    fathers_number = models.IntegerField()
    mothers_name = models.CharField(max_length=100)
    mothers_number = models.IntegerField()
    delete_status = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)
    # admission_date = models.DateField()

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(TPersonData, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        indexes = [
            models.Index(
                name="m_person_data_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "m_person_data"


class TTeacher(models.Model):
    person_data = models.ForeignKey(TPersonData, models.DO_NOTHING)
    standard_class = models.ForeignKey(TStandardClass, models.DO_NOTHING)
    subject = models.ForeignKey(MSubject, models.DO_NOTHING)
    activate = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(TTeacher, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.person_data)

    class Meta:
        indexes = [
            models.Index(
                name="t_teacher_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "t_teacher"


class TStudent(models.Model):
    person_data = models.ForeignKey(TPersonData, models.DO_NOTHING)
    standard_class = models.ForeignKey(TStandardClass, models.DO_NOTHING)
    activate = models.BooleanField(blank=True, null=True)
    created_user_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_user_id = models.CharField(max_length=100)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.person_data)

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        _utils = Utils()
        if not self.id:
            self.created_at = _utils.get_timestamp()
        self.updated_at = _utils.get_timestamp()
        return super(TStudent, self).save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(
                name="t_student_index",
                fields=["id"],
            )
        ]
        managed = True
        db_table = "t_student"
