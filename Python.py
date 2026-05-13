import requests
from bs4 import BeautifulSoup
from supabase import create_client

# Configurações do seu Supabase
URL_SUPABASE = "SUA_URL_AQUI"
KEY_SUPABASE = "SUA_CHAVE_ANON_AQUI"
supabase = create_client(URL_SUPABASE, KEY_SUPABASE)

def salvar_no_banco(canal, origem, autor, texto, data, sentimento, link):
    dados = {
        "canal": canal,
        "plataforma_origem": origem,
        "autor": autor,
        "conteudo": texto,
        "data_publicacao": data,
        "sentimento": sentimento,
        "link_referencia": link
    }
    supabase.table("monitoramento_global").insert(dados).execute()

# --- MÓDULO DE BLOGS E PORTAIS DE TECNOLOGIA ---
def monitorar_web(termo):
    print(f"Buscando '{termo}' em portais de notícias...")
    # Exemplo com o Google News (RSS)
    url = f"https://news.google.com/rss/search?q={termo}&hl=pt-PT&gl=AO&ceid=AO:pt-150"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    
    for item in soup.find_all('item'):
        salvar_no_banco(
            canal="Google Notícias / Portais",
            origem=item.source.text if item.source else "Web",
            autor="Redação",
            texto=item.title.text,
            data=item.pubDate.text,
            sentimento="Neutro", # IA pode analisar depois
            link=item.link.text
        )

# --- MÓDULO DE SIMULAÇÃO (REDES SOCIAIS E RÁDIO) ---
# Aqui você integraria as APIs oficiais conforme as chaves de acesso
def monitorar_redes_sociais(termo):
    # Lógica para Facebook, TikTok e YouTube via API
    print(f"Sincronizando menções de {termo} no YouTube e Facebook...")
    pass 

# Execução principal
if __name__ == "__main__":
    MEU_TERMO = "SuaEmpresaOuConcorrente"
    monitorar_web(MEU_TERMO)
    print("Captura concluída! Verifique seu dashboard no Supabase.")
  
