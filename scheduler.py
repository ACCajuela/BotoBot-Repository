from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import timedelta

scheduler = AsyncIOScheduler()


def agendar_lembrete(bot, canal_id, deadline, descricao, roles):
    lembrete_time = deadline - timedelta(hours=1)
    scheduler.add_job(
        enviar_lembrete, 'date', run_date=lembrete_time,
        args=[bot, canal_id, descricao, roles]
    )

async def enviar_lembrete(bot, canal_id, descricao, mentions_list):
    canal = bot.get_channel(canal_id)
    if canal:
        await canal.send(
            f"🔔 Lembrete: **{descricao}** para {' '.join(mentions_list)} vence em 1h!"
        )

