SampleIndex = {"carmeli"}
#kmc=/data/00/user/user214/miniconda3/envs/snakemake/bin/kmc
#genomewcope=/data/00/user/user214/miniconda3/envs/snakemake/bin/genomescope2
rule all:
    input:
        expand("{sample}/summary.txt", sample = SampleIndex)
rule kmc:
    input:
        "{sample}.1.fastq",
        "{sample}.2.fastq"
    output:
        "{sample}.histo"
    params:
        "{sample}_tmp"
    shell:
        """
        mkdir {params} ;
        ls {input[0]} {input[1]} > FILES ;
        kmc -k21 -t10 -m64 -ci1 -cs10000 @FILES reads {params}/  ;
        kmc_tools transform reads histogram {output} -cx10000 ;
        """
rule genomescope:
    input:
        "{sample}.histo"
    output:
        "{sample}/summary.txt"
    params:
        "{sample}"
    shell:
        "genomescope2 -i {input} -o {params} -t 21 ; ll {output}"
