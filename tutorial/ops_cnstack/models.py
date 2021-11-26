from django.db import models

# Create your models here.

CPU_TYPE = [
    ("x86", "X86"),
    ("arm", "ARM"),
]


class EnvList(models.Model):
    ENV_STATUS = [
        ("waiting", "待配置"),  # 等待创建slb等
        ("using", "使用中"),
        ("deleted", "已释放"),
    ]

    USE_FOR = [
        ("研发自测", "研发自测"),
        ("高可用测试", "高可用测试"),
        ("长稳测试", "长稳测试"),
        ("性能测试", "性能测试"),
        ("功能测试", "功能测试"),
        ("PIPELINE", "PIPELINE"),
        ("交付演练", "交付演练"),
        ("运维演练", "运维演练"),
        ("E2E演练", "E2E演练"),
        ("HOTFIX演练", "HOTFIX演练"),
        ("安全扫描", "安全扫描"),
        ("其他", "其他"),
    ]
    name = models.CharField(primary_key=True, max_length=128)
    status = models.CharField(
        choices=ENV_STATUS, default="waiting", max_length=16)  # 是否释放
    version = models.CharField(max_length=256, blank=True)  # 版本
    cpu_type = models.CharField(choices=CPU_TYPE, default="x86", max_length=16)
    owner_info = models.JSONField(blank=True, default=dict)
    proxy_info = models.JSONField(blank=True, default=dict)
    node_type = models.CharField(blank=True, max_length=16)
    nodes_info = models.JSONField(blank=True, default=dict)  # 底座集群机器信息
    region = models.CharField(blank=True, max_length=32)
    res_usage = models.CharField(blank=True, max_length=32)
    zone = models.CharField(blank=True, max_length=128)
    vpc_id = models.CharField(blank=True, max_length=128)
    use_for = models.CharField(
        choices=USE_FOR, blank=True, default="", max_length=128)  # 用途
    user = models.CharField(blank=True, max_length=256)  # 使用者
    user_type = models.CharField(blank=True, max_length=256)  # 使用者类型
    ding_token = models.CharField(max_length=128, blank=True)  # DingDing token
    ding_secret = models.CharField(
        max_length=128, blank=True)  # DingDing secret
    slb_info = models.JSONField(blank=True, default=dict)  # SLB信息
    announcement_info = models.TextField(blank=True, default="")  # 自动生成的公告信息
    created_at = models.DateTimeField(blank=True)  # 这个手动传
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.name
