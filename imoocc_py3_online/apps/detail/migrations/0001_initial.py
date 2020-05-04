# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CabinetInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cab_name', models.CharField(verbose_name='机柜编号', max_length=10)),
                ('cab_lever', models.CharField(verbose_name='机器U数,1-10分别代表1~10层', max_length=2)),
            ],
            options={
                'verbose_name': '机柜信息表',
                'verbose_name_plural': '机柜信息表',
                'db_table': 'cabinetinfo',
            },
        ),
        migrations.CreateModel(
            name='ConnectionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ssh_username', models.CharField(verbose_name='ssh用户名', max_length=10, null=True, default='')),
                ('ssh_userpasswd', models.CharField(verbose_name='ssh用户密码', max_length=40, null=True, default='')),
                ('ssh_hostip', models.CharField(verbose_name='ssh登录的ip', max_length=40, null=True, default='')),
                ('ssh_host_port', models.CharField(verbose_name='ssh登录的端口', max_length=10, null=True, default='')),
                ('ssh_rsa', models.CharField(verbose_name='ssh私钥', max_length=64, default='')),
                ('rsa_pass', models.CharField(verbose_name='私钥的密钥', max_length=64, default='')),
                ('ssh_status', models.IntegerField(verbose_name='用户连接状态,0-登录失败,1-登录成功', default=0)),
                ('ssh_type', models.IntegerField(verbose_name='用户连接类型, 1-rsa登录,2-dsa登录,3-ssh_rsa登录,4-docker成功,5-docker无法登录', default=0)),
                ('sn_key', models.CharField(verbose_name='唯一设备ID', max_length=256, default='')),
            ],
            options={
                'verbose_name': '用户登录信息表',
                'verbose_name_plural': '用户登录信息表',
                'db_table': 'connectioninfo',
            },
        ),
        migrations.CreateModel(
            name='NetConnectionInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tel_username', models.CharField(verbose_name='用户名', max_length=10, null=True, default='')),
                ('tel_userpasswd', models.CharField(verbose_name='设备用户密码', max_length=40, null=True, default='')),
                ('tel_enpasswd', models.CharField(verbose_name='设备超级用户密码', max_length=40, null=True, default='')),
                ('tel_host_port', models.CharField(verbose_name='设备登录的端口', max_length=10, null=True, default='')),
                ('tel_hostip', models.CharField(verbose_name='设备登录的ip', max_length=40, null=True, default='')),
                ('tel_status', models.IntegerField(verbose_name='用户连接状态,0-登录失败,1-登录成功', default=0)),
                ('tel_type', models.IntegerField(verbose_name='用户连接类型, 1-普通用户可登录,2-超级用户可登录', default=0)),
                ('sn_key', models.CharField(verbose_name='唯一设备ID', max_length=256, default='')),
            ],
            options={
                'verbose_name': '网络设备用户登录信息',
                'verbose_name_plural': '网络设备用户登录信息',
                'db_table': 'netconnectioninfo',
            },
        ),
        migrations.CreateModel(
            name='NetWorkInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('host_ip', models.CharField(verbose_name='网络设备ip', max_length=40)),
                ('host_name', models.CharField(verbose_name='网络设备名', max_length=10)),
                ('sn', models.CharField(verbose_name='SN－设备的唯一标识', max_length=256, default='')),
                ('net_cab', models.ForeignKey(to='detail.CabinetInfo')),
            ],
            options={
                'verbose_name': '网络设备表',
                'verbose_name_plural': '网络设备表',
                'db_table': 'networkinfo',
            },
        ),
        migrations.CreateModel(
            name='OtherMachineInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ip', models.CharField(verbose_name='设备ip', max_length=40)),
                ('sn_key', models.CharField(verbose_name='设备的唯一标识', max_length=256)),
                ('machine_name', models.CharField(verbose_name='设备名称', max_length=20)),
                ('remark', models.TextField(verbose_name='备注', default='')),
                ('reson_str', models.CharField(verbose_name='归纳原因', max_length=128, default='')),
                ('oth_cab', models.ForeignKey(to='detail.CabinetInfo')),
            ],
            options={
                'verbose_name': '其它设备表',
                'verbose_name_plural': '其它设备表',
                'db_table': 'othermachineinfo',
            },
        ),
        migrations.CreateModel(
            name='PhysicalServerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('server_ip', models.CharField(verbose_name='服务器IP', max_length=40)),
                ('machine_brand', models.CharField(verbose_name='服务器品牌', max_length=60, default='--')),
                ('system_ver', models.CharField(verbose_name='操作系统版本', max_length=30, default='')),
                ('sys_hostname', models.CharField(verbose_name='操作系统主机名', max_length=15)),
                ('mac', models.CharField(verbose_name='MAC地址', max_length=512, default='')),
                ('sn', models.CharField(verbose_name='SN-主机的唯一标识', max_length=256, default='')),
                ('vir_type', models.CharField(verbose_name='宿主机类型', max_length=2, default='')),
                ('conn_phy', models.ForeignKey(to='detail.ConnectionInfo')),
            ],
            options={
                'verbose_name': '物理服务器信息表',
                'verbose_name_plural': '物理服务器信息表',
                'db_table': 'physicalserverinfo',
            },
        ),
        migrations.CreateModel(
            name='StatisticsRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('datatime', models.DateTimeField(verbose_name='更新时间', default='2020-02-12')),
                ('all_count', models.IntegerField(verbose_name='所有设备数量', default=0)),
                ('pyh_count', models.IntegerField(verbose_name='物理设备数量', default=0)),
                ('net_count', models.IntegerField(verbose_name='网络设备数量', default=0)),
                ('other_count', models.IntegerField(verbose_name='其他设备数量', default=0)),
                ('kvm_count', models.IntegerField(verbose_name='KVM设备数量', default=0)),
                ('docker_count', models.IntegerField(verbose_name='Docker设备数量', default=0)),
                ('vmx_count', models.IntegerField(verbose_name='VMX设备数量', default=0)),
            ],
            options={
                'verbose_name': '扫描后的汇总硬件统计信息',
                'verbose_name_plural': '扫描后的汇总硬件统计信息',
                'db_table': 'statisticsrecord',
            },
        ),
        migrations.CreateModel(
            name='VirtualServerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('server_ip', models.CharField(verbose_name='服务器IP', max_length=40)),
                ('server_type', models.CharField(verbose_name='服务器类型:kvm,Vmware,Docker,others', max_length=80, default='')),
                ('system_ver', models.CharField(verbose_name='操作系统版本', max_length=30, default='')),
                ('sys_hostname', models.CharField(verbose_name='操作系统主机名', max_length=15)),
                ('mac', models.CharField(verbose_name='MAC地址', max_length=512, default='')),
                ('sn', models.CharField(verbose_name='SN-主机的唯一标识', max_length=256, default='')),
                ('conn_vir', models.ForeignKey(to='detail.ConnectionInfo')),
                ('vir_phy', models.ForeignKey(to='detail.PhysicalServerInfo')),
            ],
            options={
                'verbose_name': '虚拟设备表',
                'verbose_name_plural': '虚拟设备表',
                'db_table': 'virtualserverinfo',
            },
        ),
        migrations.AddField(
            model_name='netconnectioninfo',
            name='dev_info',
            field=models.ForeignKey(to='detail.NetWorkInfo'),
        ),
    ]
