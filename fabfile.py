from fabric.api import env, cd, prefix, local, run

# nombre de la máquina de producción
env.hosts = ["cloud"]
# env.user
# env.password


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/mkdocs/bin/activate"):
      with cd("~/mkdocss"):
          run("git pull")
	  run("mkdocs build")
