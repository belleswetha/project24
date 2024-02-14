from django.db import models

# Create your models here.
class Dept(models.Model):
    dname=models.CharField(max_length=100)
    deptno=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.dname
    
class Employee(models.Model):
    deptno=models.OneToOneField(Dept,on_delete=models.CASCADE)
    ename=models.CharField(max_length=100,primary_key=True)
    empno=models.IntegerField()
    job=models.CharField(max_length=100)
    sal=models.IntegerField()

    def __str__(self):
        return self.ename
    
class salgrade(models.Model):
    ename=models.OneToOneField(Employee,on_delete=models.CASCADE)
    sal=models.IntegerField()
    hisal=models.IntegerField()
    losal=models.IntegerField()
    def __str__(self):
        return self.sal


class Bonus(models.Model):
    fevbonus=models.IntegerField()
    pbonus=models.IntegerField()
    
    
    


