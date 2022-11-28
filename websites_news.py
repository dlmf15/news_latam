from datetime import datetime
import pandas as pd
import requests

df = pd.read_csv('/Users/devalou/PycharmProjects/news_latam/mean_table_final.csv', delimiter=';')
# dfd = df.copy()
dfd = df[10:11]


def websites_search(row_info, file):
    sites = {
            'argentina': '(site:https://www.infobae.com/ | site:https://elintransigente.com/ | site:https://www.clarin.com/ | site:https://www.lanacion.com.ar/ | site:https://www.ellitoral.com/ | site:https://www.pagina12.com.ar/ | site:https://diariopanorama.com/ | site:https://www.telam.com.ar/ | site:https://www.perfil.com/ | site:https://misionesonline.net/ | site:https://www.ambito.com/ | site:https://www.cronista.com/ | site:https://www.lavoz.com.ar/ | site:https://www.minutouno.com/ | site:https://www.elliberal.com.ar/ | site:https://www.iprofesional.com/ | site:https://www.mdzol.com/ | site:https://www.eldestapeweb.com/ | site:https://www.losandes.com.ar/ | site:https://www.eldia.com/)',
            'bolivia': '(site:https://eldeber.com.bo/ | site:https://www.lostiempos.com/ | site:https://www.paginasiete.bo/ | site:https://eju.tv/ | site:https://www.la-razon.com/ | site:https://www.opinion.com.bo/ | site:https://www.eldiario.net/ | site:https://correodelsur.com/ | site:https://notibol.com/ | site:https://abi.bo/ | site:https://www.la-epoca.com.bo/ | site:http://erbol.com.bo/ | site:https://www.noticiasfides.com/ | site:http://www.boliviatv.bo/ | site:https://www.bolivia.com/ | site:http://urgente.bo/ | site:https://www.eldia.com.bo/ | site:https://www.boliviaentusmanos.com/ | site:https://elpotosi.net/ | site:https://jornada.com.bo/)',
            'brazil': '(site:https://www.uol.com.br/ | site:https://oglobo.globo.com/ | site:https://www.gazetaweb.com/ | site:https://g1.globo.com/ | site:https://www.campograndenews.com.br/ | site:https://noticias.uol.com.br/ | site:https://www.terra.com.br/ | site:https://www.folha.uol.com.br/ | site:https://www.meiahora.com.br/ | site:https://odia.ig.com.br/ | site:https://www.r7.com/ | site:https://www.estadao.com.br/ | site:https://www.brasil247.com/ | site:https://istoe.com.br/ | site:https://www.gazetadopovo.com.br/ | site:https://www.correiobraziliense.com.br/ | site:https://www.otempo.com.br/ | site:https://ne10.uol.com.br/ | site:https://revistaforum.com.br/ | site:https://www.opovo.com.br/)',
            'chile': '(site:https://www.biobiochile.cl/ | site:https://www.adnradio.cl/ | site:https://www.latercera.com/ | site:https://www.emol.com/ | site:https://www.df.cl/ | site:https://www.cooperativa.cl/ | site:https://www.elmostrador.cl/ | site:https://www.24horas.cl/ | site:https://www.publimetro.cl/ | site:https://www.lacuarta.com/ | site:https://www.eldinamo.cl/ | site:https://www.soychile.cl/ | site:https://www.diarioconcepcion.cl/ | site:https://www.elciudadano.com/ | site:http://www.lanacion.cl/ | site:https://cambio21.cl/ | site:http://www.diarioeldia.cl/ | site:https://www.elobservatodo.cl/ | site:http://www.chanarcillo.cl/ | site:https://www.puranoticiachile.cl/)',
            'colombia': '(site:https://www.las2orillas.co/ | site:https://www.eltiempo.com/ | site:https://www.semana.com/ | site:https://www.elespectador.com/ | site:https://www.larepublica.co/ | site:https://www.minuto30.com/ | site:https://caracol.com.co/ | site:https://www.portafolio.co/ | site:https://www.elcolombiano.com/ | site:https://www.rcnradio.com/ | site:https://www.elheraldo.co/ | site:https://hsbnoticias.com/ | site:https://www.elpais.com.co/ | site:https://www.vanguardia.com/ | site:https://lasillavacia.com/ | site:https://www.colombia.com/ | site:https://www.publimetro.co/ | site:https://boyaca.extra.com.co/ | site:https://www.eluniversal.com.co/ | site:https://www.noticiasrcn.com/)',
            'ecuador': '(site:https://www.eluniverso.com/ | site:https://www.elcomercio.com/ | site:https://www.vistazo.com/ | site:https://www.eltelegrafo.com.ec/ | site:https://www.expreso.ec/ | site:https://www.metroecuador.com.ec/ | site:https://www.lahora.com.ec/ | site:https://www.extra.ec/ | site:https://www.larepublica.ec/ | site:https://www.eldiario.ec/ | site:https://elmercurio.com.ec/ | site:http://ecuadorenvivo.com/ | site:https://www.ultimasnoticias.ec/ | site:https://diariocorreo.com.ec/ | site:https://www.elnorte.ec/ | site:https://cronica.com.ec/ | site:https://www.diariolosandes.com.ec/ | site:https://www.elheraldo.com.ec/ | site:http://diariopinion.com/ | site:https://lanacion.com.ec/)',
            'mexico': '(site:https://www.eluniversal.com.mx/ | site:https://www.milenio.com/ | site:https://www.sdpnoticias.com/ | site:https://www.elfinanciero.com.mx/ | site:https://www.excelsior.com.mx/ | site:https://www.reforma.com/ | site:https://www.eleconomista.com.mx/ | site:https://jornada.com.mx/ | site:https://www.yucatan.com.mx/ | site:https://www.elnorte.com/ | site:https://www.radioformula.com.mx/ | site:https://www.elsiglodetorreon.com.mx/ | site:https://www.sinembargo.mx/ | site:https://aristeguinoticias.com/ | site:https://www.proceso.com.mx/ | site:https://www.informador.mx/ | site:https://www.sopitas.com/ | site:https://www.expreso.com.mx/ | site:https://diario.mx/ | site:https://vanguardia.com.mx/)',
            'peru': '(site:https://elcomercio.pe/ | site:https://larepublica.pe/ | site:https://gestion.pe/ | site:https://peru21.pe/ | site:https://elperuano.pe/ | site:https://andina.pe/ | site:https://diariocorreo.pe/ | site:https://libero.pe/ | site:https://elbocon.pe/ | site:https://trome.pe/ | site:https://ojo.pe/ | site:https://www.expreso.com.pe/ | site:https://exitosanoticias.pe/ | site:https://www.latina.pe/ | site:https://elpopular.pe/ | site:https://peru.com/ | site:https://laprensa.peru.com/ | site:https://larazon.pe/ | site:https://lamula.pe/ | site:https://caretas.pe/)'
            }
    brand_df = pd.DataFrame(columns=['brand name', 'argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador',
                                     'mexico', 'peru'])
    brand_name_year = []

    for year in range(13, 21):  # create 'brand_name' column with years from 2013 to 2020
        brand_name_year.append(row_info['brand_name']+'_'+str(year))
    brand_df['brand name'] = brand_name_year
#  'argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'mexico',
    for country in ['argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'mexico', 'peru']:
        if row_info[country] == 'Si':
            query_result = []
            for year in ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']:
                params = {
                    'api_key': '',
                    #'search_type': 'news',
                    # 'location': country,
                    'q': row_info['query'] + ' ' + sites[country] + ' before:{}-01-01 after:{}-01-01'.format(int(year) + 1, year),
                    'output': 'csv',
                    'csv_fields': 'search_information.total_results,search_information.original_query_yields_zero_results'
                }
                #  print(params['q'])
                api_result = requests.get('https://api.valueserp.com/search', params)
                num_searches = api_result.text.split('\n')[-1].split(',')[0]
                no_result = api_result.text.split('\n')[-1].split(',')[1]

                if no_result == 'true':
                    query_result.append(0)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0,
                          file=file)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0)


                elif num_searches == '':  # if didn't get any results
                    query_result.append(0)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0,
                          file=file)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ', 0)
                else:  # turn into int
                    query_result.append(int(num_searches))
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ',
                          num_searches, file=file)
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], year, ': ',
                          num_searches)

            brand_df[country] = query_result
        else:
            brand_df[country] = ['x' for i in range(13, 21)]
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], ': ', 'x', file=file)
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), country, row_info['brand_name'], ': ', 'x')
    return brand_df


f = open('web_news_log_1.txt', 'a')
for name, group in dfd.groupby('company'):

    result_df = pd.DataFrame(columns=['brand name', 'argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador',
                                      'mexico', 'peru'])
    for index in range(len(group.index)):
        company = group.iloc[index]['company']
        result_df = pd.concat([result_df, websites_search(group.iloc[index], f)])
    # to_excel
    # print(result_df)
    result_df.to_excel('/Users/devalou/PycharmProjects/news_latam/webnews/{}_webnews.xlsx'.format(name), sheet_name=name
                       , index=False)
