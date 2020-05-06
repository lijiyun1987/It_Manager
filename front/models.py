from django.db import models

class Machine(models.Model):
    mac_id = models.CharField(max_length=10, unique=True)
    vender = models.CharField(max_length=50)
    mac_type = models.CharField(max_length=50)
    model_id = models.CharField(max_length=50, blank=True)
    mac_sn = models.CharField(max_length=50)
    use_des = models.TextField(blank=True)
    location = models.CharField(max_length=50)
    ipmi = models.GenericIPAddressField(protocol='ipv4')
    level = models.CharField(max_length=10)

    class Meta:
        db_table = 'machine'
        ordering = ["mac_id"]

    def __str__(self):
        return self.mac_id

class OpsLog(models.Model):
    ops_obj = models.CharField(max_length=50)
    ops_subject = models.CharField(max_length=200)
    ops_log = models.TextField()
    des = models.CharField(max_length=200, blank=True)
    date = models.DateField()

    class Meta:
        db_table = 'OpsLog'
        ordering = ["date"]

    def __str__(self):
        return self.ops_subject

class Maintenance(models.Model):
    mac_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    problem_des = models.TextField()
    solution = models.TextField()
    results = models.BooleanField(default=True)
    new_pn = models.CharField(max_length=20)
    new_sn = models.CharField(max_length=20)
    old_pn = models.CharField(max_length=20)
    old_sn = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        db_table = 'Maintenance'
        ordering = ["date"]

    def __str__(self):
        return self.subject
