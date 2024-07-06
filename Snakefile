rule figure1:
    output:
        directory("src/data/Figure1")
    conda:
        "environment.yml"
    cache:
        True
    script:
        "src/scripts/run_ebtel_figure1.py"
rule figure2:
    output:
        directory("src/data/Figure2")
    conda:
        "environment.yml"
    cache:
        True
    script:
        "src/scripts/run_ebtel_figure2.py"
rule figure3:
    output:
        directory("src/data/Figure3")
    conda:
        "environment.yml"
    cache:
        True
    script:
        "src/scripts/run_ebtel_figure3.py"
