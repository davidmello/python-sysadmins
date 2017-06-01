#!/usr/bin/python
# -*- coding: utf-8 -*-

import boto3

ec2 = boto3.resource("ec2")

def running_instances():
	# instances = ec2.instances.all()
	instances = ec2.instances.filter(Filters=[{"Name":"instance-state-name","Values":["running"]}])
	for i in instances:
		print i.id, i.instance_type

def new_instance():
	# new_instance = ec2.create_instances(ImageId="ami-b2e3c6d8",MinCount=1,MaxCount=1)
	new_instance = ec2.create_instances(ImageId="ami-b2e3c6d8",MinCount=1,MaxCount=1,SecurityGroupIds=['sg-0f90a071'])
	print new_instance

def stop_instance(id):
	stop_instance = ec2.instances.filter(InstanceIds=[id]).stop()
	print stop_instance

def terminate_instance(id):
	terminate_instance = ec2.instances.filter(InstanceIds=[id]).terminate()
	print terminate_instance

def list_security_groups():
	list_security_groups = ec2.instances.filter(Filters=[SecurityGroups()])
	print list_security_groups

def create_security_group(name):
	sg = ec2.create_security_group(GroupName=name,Description="Grupo criado atraves do boto3")

def add_rule():
	sg = ec2.SecurityGroup('sg-0f90a071')
	sg.authorize_ingress(FromPort=80,ToPort=80,CidrIp="0.0.0.0/0",IpProtocol="tcp")
	print sg

def remove_rule():
	sg = ec2.SecurityGroup('sg-0f90a071')
	sg.revoke_ingress(FromPort=80,ToPort=80,CidrIp="0.0.0.0/0",IpProtocol="tcp")
	print sg


if __name__ == '__main__':
	# new_instance()	
	# stop_instance('i-0de9335dfa432b018')
	# terminate_instance('i-08ed4432475afac65')
	# create_security_group('David')
	# list_security_groups()
	# add_rule()
	remove_rule()

