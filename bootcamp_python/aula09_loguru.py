from loguru import logger

logger.debug("Log de debug - Geralmente utilizado para informar ou relembrar algo")
logger.info("Log de info - Geralmente utilizado para informações relevantes")
logger.warning("Log de aviso - Geralmente utilizado para informar que algo pode dar errado (ex de uso: mensagens que uma biblioteca ou função será descontinuada)")
logger.error("Log de erro - Geralmente utilizado para reportar erros")
logger.critical("Log crítico - Geralmente utilizado quando acontece algo que aborta a aplicação")