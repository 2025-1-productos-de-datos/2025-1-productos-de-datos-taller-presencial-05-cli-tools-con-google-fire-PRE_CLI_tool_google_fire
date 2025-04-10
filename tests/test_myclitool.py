"""Autograding script."""

import subprocess


def test_c1_s1():
    result = subprocess.run(
        ["python3", "-m", "_solution.myclitool", "command1", "run", "1"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "---> Ejecutando command 1 subcommand 1: a = 1" in result.stdout


def test_c1_s2():
    result = subprocess.run(
        ["python3", "-m", "_solution.myclitool", "command1", "stop", "2"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "---> Ejecutando command 1 subcommand 2: b = 2" in result.stdout


def test_c2_s1():
    result = subprocess.run(
        ["python3", "-m", "_solution.myclitool", "command2", "jump", "3"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "---> Ejecutando command 2 subcommand 1: c = 3" in result.stdout


def test_c2_s2():
    result = subprocess.run(
        ["python3", "-m", "_solution.myclitool", "command2", "cry", "4"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "---> Ejecutando command 2 subcommand 2: d = 4" in result.stdout