from sigma.collection import SigmaCollection
from sigma.pipelines.sysmon import sysmon_pipeline
from sigma.pipelines.windows import windows_logsoure_pipeline, windows_audit_pipeline
from sigma.processing.resolver import ProcessingPipelineResolver
from sigma.backends.pd_df import pd_df

def convert_rule(backend, rule):
    try:
        return backend.convert_rule(rule, "pdninja")[0]
    except Exception as e:
        print(e)

def ruleset_generator(name, output_filename, input_rules, pipelines):
    print (f'''[+] Initialisation ruleset : {name} ''')
    piperesolver = ProcessingPipelineResolver()

    for pipeline in pipelines:
        piperesolver.add_pipeline_class(pipeline)
    
    combined_piepline = piperesolver.resolve(piperesolver.pipelines)
    pd_df_backend = pd_df.PandasDataFramePythonBackend(combined_piepline)
