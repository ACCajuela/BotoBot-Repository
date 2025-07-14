from discord.ext import commands
from datetime import datetime
from db_ops import create_task, list_tasks
from scheduler import agendar_lembrete

@commands.command(name="addtask")
async def add_task(ctx, deadline_str, *args):
    try:
        deadline = datetime.strptime(deadline_str, "%d/%m/%Y %H:%M")
    except ValueError:
        await ctx.send("❌ Data inválida. Use o formato `DD-MM-AAAA HH:MM`")
        return

    if len(args) < 2:
        await ctx.send("❌ Você precisa mencionar ao menos um responsável e escrever a descrição.")
        return

    mentions = []
    description_words = []

    for arg in args:
        if arg.startswith("<@") or arg.startswith("<@&"):
            mentions.append(arg)
        else:
            description_words.append(arg)

    if not mentions:
        await ctx.send("❌ Você precisa mencionar pelo menos um cargo ou usuário responsável.")
        return

    description = " ".join(description_words)

    task_id = await create_task(description, deadline, mentions)
    await ctx.send(f"✅ Tarefa #{task_id} criada para {', '.join(mentions)} até `{deadline}`")

    agendar_lembrete(ctx.bot, ctx.channel.id, deadline, description, mentions)

@commands.command(name="listtasks")
async def list_tasks_command(ctx):
    tasks = await list_tasks()

    if not tasks:
        await ctx.send("📭 Nenhuma tarefa cadastrada.")
        return
    
    deadline_format = task.deadline.strftime("%d/%m/%Y %H:%M")

    message_lines = ["📋 **Tarefas cadastradas:**"]
    for task in tasks:
        message_lines.append(
            f"🗓 `{deadline_format}` - **{task.description}** → {task.roles}"
        )

    await ctx.send("\n".join(message_lines))
