def define_env(env):
    @env.macro
    def time(t):
        return f'<span class="local-time" data-utc="{t}">{t} UTC</span>'