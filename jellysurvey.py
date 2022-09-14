###jellyfish=/data/01/user214/yanshu/survey/jellyfish
###genomescope2=/data/00/user/user214/miniconda3/envs/snakemake/bin/genomescope2
SAMLIST="carmeli"
rule all:
    input :
        expand("{sample}/summary.txt",sample=SAMLIST)
rule jell:
    input:
        "{sample}.1.fastq",
        "{sample}.2.fastq"
    output:
        "{sample}.jf"
    shell:
        "jellyfish count -C -m 21 -s 1000000000 -t 10 {input[0]} {input[1]} -o {output[0]}"
rule kmer:
    input:
        "{sample}.jf"
    output:
        "{sample}.histo"
    shell:
        "jellyfish histo -t 10 {input[0]} > {output[0]}"
rule genomescope:
    input:
        "{sample}.histo"
    output:
        "{sample}/summary.txt"
    params:
        "{sample}"
    shell:
        "genomescope2 -i {input} -o {params} -t 21 " 

##produced by kogoori  masaki
