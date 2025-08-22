from fixtures import (
    get_driver,
    Functions    
)
import os


def before_all(context):
    context.brw              = get_driver()
    
    commands                 = Functions(context.brw)

    context.click            = commands.click
    context.type             = commands.send_keys
    context.validate_text    = commands.validate_text
    context.validate_popup   = commands.validate_popup_message


def after_all(context):
    context.brw.quit()

def before_scenario(context,scenario):
    context.scenario_name = scenario.name

def after_step(context,step):
    if step.status.name != 'passed':
        os.makedirs('screenshots',exist_ok=True)

        scenario_folder = context.scenario_name[:-9].replace(' ','_').replace('.','').replace(',','').replace('-','_')
        os.makedirs(f'screenshots/{scenario_folder}',exist_ok=True)


        step_name = step.name.replace(' ','_').replace(',','').replace('.','')
        context.brw.save_screenshot(f'./screenshots/{scenario_folder}/{step_name}.png')
