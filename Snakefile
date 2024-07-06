rule sim_figure1:
    output:
        directory("src/data/Figure1")
    conda:
        "environment.yml"
    cache:
        True
    script:
        "src/scripts/run_ebtel_figure1.py"
rule sim_figure2:
    output:
        directory("src/data/Figure2")
    conda:
        "environment.yml"
    cache:
        True
    script:
        "src/scripts/run_ebtel_figure2.py"
rule sim_figure3:
    output:
        directory("src/data/Figure3")
    conda:
        "environment.yml"
    cache:
        True
    script:
        "src/scripts/run_ebtel_figure3.py"
rule plot_figure1:
    input:
        "src/data/Figure1"
    conda:
        "environment.yml"
    script:
        "src/scripts/render_figure1.py"
rule plot_figure2:
    input:
        "src/data/Figure2"
    conda:
        "environment.yml"
    script:
        "src/scripts/render_figure2.py"
rule plot_figure3:
    input:
        "src/data/Figure3"
    conda:
        "environment.yml"
    script:
        "src/scripts/render_figure3.py"
