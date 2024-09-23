#!/usr/bin/env python3
import click
import os
import sys
import signal
import subprocess
from prettytable import PrettyTable
from core.container.container import Container as core_container
from core.edgecam.edgecam import Edgecam as core_edgecam
# from core.module.module import Module as core_module
from core.system.cpu import Cpu
from core.system.gpu import Gpu
from core.system.memory import Memory
from core.system.storage import Storage
from util.config import load

@click.group()
def cli():
    pass

@cli.command()
def start():
    """대시보드를 시작합니다."""
    click.echo('대시보드를 시작합니다.')
    os.system("uvicorn main:app")

@cli.command()
def stop():
    """대시보드를 중지합니다."""
    click.echo('대시보드를 중지합니다.')
    port = 8000
    try:
        if os.name == 'posix':  # Linux/Unix/Mac
            # 1. Find the PID of the process using the port
            result = subprocess.run(
                ["lsof", "-i", f":{port}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode != 0:
                print(f"포트 {port}에서 프로세스를 찾을 수 없습니다.")
                return
            
            # Parsing the result to find the PID
            lines = result.stdout.splitlines()
            if len(lines) < 2:
                print(f"포트 {port}에서 실행 중인 프로세스가 없습니다.")
                return
            
            pid = int(lines[1].split()[1])
            print(f"PID {pid}를 종료합니다.")
            
            # 2. Kill the process using the PID
            os.kill(pid, signal.SIGTERM)
            print(f"프로세스 {pid}가 종료되었습니다.")
        elif os.name == 'nt':
            # 1. Find the PID of the process using the port
            result = subprocess.run(
                ["netstat", "-ano", "|", "findstr", f":{port}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )
            
            if result.returncode != 0:
                print(f"포트 {port}에서 프로세스를 찾을 수 없습니다.")
                return
            
            lines = result.stdout.splitlines()
            if len(lines) == 0:
                print(f"포트 {port}에서 실행 중인 프로세스가 없습니다.")
                return
            
            # Parsing the result to find the PID
            pid = int(lines[0].strip().split()[-1])
            print(f"PID {pid}를 종료합니다.")
            
            # 2. Kill the process using the PID
            subprocess.run(["taskkill", "/F", "/PID", str(pid)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"프로세스 {pid}가 종료되었습니다.")
        else:
            print("지원하지 않는 운영체제입니다.")
    
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    

@cli.command()
def status():
    """대시보드 상태를 확인합니다."""
    click.echo('대시보드 상태를 확인합니다.')
    port = 8000
    try:
        if os.name == 'posix':  # Linux/Unix/Mac
            # 1. Use 'lsof' to check for processes using the port
            result = subprocess.run(
                ["lsof", "-i", f":{port}"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode != 0:
                print(f"포트 {port}에서 실행 중인 프로세스를 찾을 수 없습니다.")
                return
            
            lines = result.stdout.splitlines()
            if len(lines) < 2:
                print(f"포트 {port}에서 실행 중인 프로세스가 없습니다.")
                return
            
            print(f"포트 {port}에서 실행 중인 프로세스 상태:")
            for line in lines[1:]:
                print(line)

        elif os.name == 'nt':  # Windows
            # 1. Use 'netstat' to check for processes using the port
            result = subprocess.run(
                ["netstat", "-ano"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )
            
            if result.returncode != 0:
                print(f"포트 {port}에서 실행 중인 프로세스를 찾을 수 없습니다.")
                return
            
            lines = result.stdout.splitlines()
            matching_lines = [line for line in lines if f":{port}" in line]
            
            if len(matching_lines) == 0:
                print(f"포트 {port}에서 실행 중인 프로세스가 없습니다.")
                return
            
            print(f"포트 {port}에서 실행 중인 프로세스 상태:")
            for line in matching_lines:
                print(line)

        else:
            print("지원하지 않는 운영체제입니다.")
    
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    
@cli.command()
def container():
    """컨테이너 상태를 확인합니다."""
    click.echo('컨테이너 상태를 확인합니다.')
    try:
        cls = core_container()
        container_name_list = ["pls-web", "pls-was", "pls-module", "pls-mysql", "pls-redis"]
        status = cls.check()
        table = PrettyTable()
        table.field_names = ["Cotainer Name", "Status"]
        for i in range(len(container_name_list)):
            cur_status = ""
            if status[i] == True:
                cur_status = "Online"
            else:
                cur_status = "Offline"
            table.add_row([container_name_list[i], cur_status])
        click.echo(table)
    
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

@cli.command()
def edgecam():
    """컨테이너 상태를 확인합니다."""
    click.echo('컨테이너 상태를 확인합니다.')
    try:
        config = load()
        cls = core_edgecam(config["edgecam"])
        status = cls.check()
        table = PrettyTable()
        table.field_names = ["Edgecam Name", "Camera", "Thermal", "Rader", "Toilet Rader"]
        for i in range(len(status)):
            if len(status) == 0 or i == len(status) -1:
                break
            cur_status = [status[i][0]]
            for j in range(1, 5):
                if status[i][j] == True:
                    cur_status.append("Online")
                elif status[i][j] == False:
                    cur_status.append("Offline")
                else:
                    cur_status.append("None")
            table.add_row(cur_status)
        click.echo(table)
    
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

@cli.command()
def system():
    """시스템 상태를 확인합니다."""
    click.echo('시스템 상태를 확인합니다.')
    try:
        cpu = Cpu()
        gpu = Gpu()
        memory = Memory()
        storage = Storage()
        
        cpu_usage = cpu.check()
        gpu_usage = gpu.check()
        memory_usage = memory.check()
        storage_usage = storage.check()
        
        click.echo("시스템 상태: CPU")
        cpu_table = PrettyTable()
        cpu_field_names = ["CPU Usage"]
        for i in range(len(cpu_usage[1])):
                cpu_field_names.append(f"Core {i + 1}")
        cpu_table.field_names = cpu_field_names
        cpu_table.add_row([f"{cpu_usage[0]}%"] + cpu_usage[1])
        click.echo(cpu_table)

        click.echo("시스템 상태: GPU")
        if gpu_usage[0] == []:
            click.echo("GPU 사용량을 확인할 수 없습니다.")
        else:
            gpu_table = PrettyTable()
            gpu_table.field_names = ["GPU", "Usage Rate", "Memory Usage Rate", "Memory Usage"]
            for i in range(len(gpu_usage[0])):
                gpu_table.add_row([gpu_usage[0][i], gpu_usage[1][i], gpu_usage[2][i], gpu_usage[3][i]])
            click.echo(gpu_table)

        click.echo("시스템 상태: Memory")
        memory_table = PrettyTable()
        memory_table.field_names = ["Memory", "Percent", "Used"]
        memory_table.add_row(["Usage", f"{memory_usage[0]}%", memory_usage[1]])
        click.echo(memory_table)

        click.echo("시스템 상태: Storage")
        storage_table = PrettyTable()
        storage_table.field_names = ["Storage", "Percent", "Used"]
        storage_table.add_row(["Usage", f"{storage_usage[0]}%", storage_usage[1]])
        click.echo(storage_table)
    
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

if __name__ == '__main__':
    cli()