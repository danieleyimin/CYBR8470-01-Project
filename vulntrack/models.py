from django.db import models

class Asset(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip_address = models.GenericIPAddressField()
    os_version = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hostname

class Vulnerability(models.Model):
    RISK_LEVELS = [
        ('LOW', 'Low'),
        ('MED', 'Medium'),
        ('HIGH', 'High'),
        ('CRIT', 'Critical'),
    ]
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('PROG', 'In Progress'),
        ('PATCH', 'Patched'),
        ('ACCEP', 'Risk Accepted'),
    ]
    
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='vulnerabilities')
    cve_id = models.CharField(max_length=50)
    cvss_score = models.FloatField()
    risk_level = models.CharField(max_length=10, choices=RISK_LEVELS)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    discovered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cve_id} on {self.asset.hostname}"