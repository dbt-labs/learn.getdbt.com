import snowflake.connector

def main(config):

    ctx = snowflake.connector.connect(
        **config
    )

    cs = ctx.cursor()

    return cs, ctx
    
