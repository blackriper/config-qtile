import schedule
from subprocess import  run
"""
ejecutar una tarea cada treinta minutos para cambiar el fondo de escritorio

"""


def change_background():
  run(
    "feh -z --bg-scale ~/Imágenes/*",
     shell=True
    )

schedule.every(30).minutes.do(change_background)

while True:
    schedule.run_pending()
