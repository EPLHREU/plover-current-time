import datetime

def meta(ctx, cmdline):
    action = ctx.new_action()
    action.text = time(cmdline)
    return action

def time(formatting):
    now = datetime.datetime.now()
    formatted = now.strftime(formatting)
    return(formatted)
