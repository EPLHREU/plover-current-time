import datetime
import locale

def meta(ctx, cmdline):
    action = ctx.new_action()
    action.text = time(cmdline)
    return action

def time(formatting):
    fmt, *new_locale = formatting.split('>>')

    current_locale = locale.getlocale()

    if new_locale:
        locale.setlocale(locale.LC_ALL, new_locale[0])

    now = datetime.datetime.now()
    formatted = now.strftime(fmt)

    locale.setlocale(locale.LC_ALL, current_locale)

    return(formatted)
