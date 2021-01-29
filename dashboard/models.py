from django.contrib.auth.models import User
from django.db import models


class VpmUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    is_availability = models.BooleanField(max_length=100, default=False)
    avatar = models.ImageField()

    def __str__(self):
        return self.user.first_name + ' - ' + self.specialization + ' - ' + str(self.is_availability)

    class Meta:
        verbose_name_plural = 'VPDS Users'


class ProjectTeam(models.Model):
    manager_Name = models.CharField(max_length=100)
    manager_id = models.IntegerField()
    member_one_Name = models.CharField(max_length=100)
    member_one_id = models.IntegerField()
    member_two_Name = models.CharField(max_length=100)
    member_two_id = models.IntegerField()
    member_three_Name = models.CharField(max_length=100)
    member_three_id = models.IntegerField()
    member_four_Name = models.CharField(max_length=100)
    member_four_id = models.IntegerField()
    member_five_Name = models.CharField(max_length=100)
    members_five_id = models.IntegerField()

    def __str__(self):
        return str(self.manager_Name) + ' - ' + str(self.manager_id)

    class Meta:
        verbose_name_plural = 'Project Teams'


class LiveProject(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    StartDate = models.DateField()
    duration = models.IntegerField()
    erd = models.FileField()
    dfd = models.FileField()
    srs = models.FileField()
    Other_Diagram = models.FileField()
    team_id = models.ForeignKey(ProjectTeam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.field + ' - ' + self.platform + ' - ' + str(self.team_id)

    class Meta:
        verbose_name_plural = 'Live Projects'

class ProjectArchive(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    startDate = models.DateField()
    subDate = models.DateField()
    status = models.CharField(max_length=10)
    duration = models.IntegerField()
    erd = models.FileField()
    dfd = models.FileField()
    srs = models.FileField()
    Other_Diagram = models.FileField()
    team_id = models.ForeignKey(ProjectTeam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.field + ' - ' + self.platform + '  - team id - ' + str(
            self.team_id) + '-' + str(self.duration)


class ProjectsOnHold(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    start_Date = models.DateField()
    form = models.DateField()
    hold_duration = models.IntegerField()
    cause = models.CharField(max_length=100)
    duration = models.IntegerField()
    erd = models.FileField()
    dfd = models.FileField()
    srs = models.FileField()
    Other_Diagram = models.FileField()
    team_id = models.ForeignKey(ProjectTeam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.field + ' - ' + self.platform + ' - team id -' + str(self.team_id) + str(
            self.duration)

    class Meta:
        verbose_name_plural = 'Projects on Hold'


class UpcomingProject(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    start_date = models.DateField()

    def __str__(self):
        return self.name + ' - ' + self.field + ' - ' + self.platform + ' - ' + str(self.start_date)


class Rating(models.Model):
    user = models.OneToOneField(VpmUser, null=True, blank=True, on_delete=models.CASCADE)
    project_completed = models.IntegerField()
    client_feedback = models.IntegerField()
    company_feedback = models.IntegerField()
    colleague_feedback = models.IntegerField()
    overall_rating = models.IntegerField()

    def __str__(self):
        return self.user.user.first_name + ' - ' + str(self.overall_rating)


class About(models.Model):
    tittle = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name_plural = 'About'


class Contact(models.Model):
    tittle = models.CharField(max_length=250)
    ph_no1 = models.CharField(max_length=13)
    ph_no2 = models.CharField(max_length=13)
    ph_no3 = models.CharField(max_length=13)
    ph_no4 = models.CharField(max_length=13)
    email1 = models.EmailField()
    email2 = models.EmailField()
    email3 = models.EmailField()
    email4 = models.EmailField()
    corp_address = models.CharField(max_length=255)

    def __str__(self):
        return self.tittle
