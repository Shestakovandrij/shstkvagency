# Генерує блог: список статей (blog) і статті (post-<key>) з блоків головної
# та src/lib/blog.json для site.mjs. Кожна стаття — окремий файл scripts/posts/<key>.py зі змінною POST.
# Запуск: python3 scripts/build_blog.py
import glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from blocks import *
from services_data import SERVICES
from services_pages import PRICES

MONTHS = {
    'uk': ['січня', 'лютого', 'березня', 'квітня', 'травня', 'червня', 'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня'],
    'pl': ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia'],
}

def human_date(iso, lang):
    y, m, d = (int(x) for x in iso.split('-'))
    return f'{d} {MONTHS[lang][m - 1]} {y}'

def load_posts():
    posts = []
    for f in sorted(glob.glob(os.path.join(HERE, 'posts', '*.py'))):
        ns = {}
        exec(open(f).read(), ns)
        posts.append(ns['POST'])
    return sorted(posts, key=lambda p: (p['date'], p['key']), reverse=True)

def block_html(b):
    kind = b[0]
    if kind == 'p':
        return f'          <p>{L(b[1], b[2])}</p>\n'
    if kind == 'h3':
        return f'          <h3>{L(b[1], b[2])}</h3>\n'
    if kind == 'ul':
        items = ''.join(f'            <li>{L(u, p)}</li>\n' for u, p in b[1])
        return f'          <ul>\n{items}          </ul>\n'
    if kind == 'card':
        return f'          <div class="doc__card"><p>{L(b[1], b[2])}</p></div>\n'
    if kind == 'table':
        head_ = ''.join(f'<th>{L(u, p)}</th>' for u, p in b[1])
        rows = ''.join('<tr>' + ''.join(f'<td>{L(u, p)}</td>' for u, p in row) + '</tr>' for row in b[2])
        return f'          <div class="doc__table-wrap"><table class="doc__table"><thead><tr>{head_}</tr></thead><tbody>{rows}</tbody></table></div>\n'
    raise ValueError('unknown block ' + kind)

def article(post):
    secs = f'''        <section class="doc__sec">
          <h2><span class="doc__num">00</span>{L('Коротка відповідь', 'W skrócie')}</h2>
          <div class="doc__card doc__lead-card"><p>{L(post['answer_uk'], post['answer_pl'])}</p></div>
        </section>
'''
    for i, s in enumerate(post['sections'], 1):
        secs += f'''        <section class="doc__sec">
          <h2><span class="doc__num">{i:02d}</span>{L(s['h2_uk'], s['h2_pl'])}</h2>
{''.join(block_html(b) for b in s['blocks'])}        </section>
'''
    return f'''    <section class="section" id="article">
      <div class="container">
        <article class="doc__body">
{secs}        </article>
      </div>
    </section>'''

def service_cta(post):
    key = post['service']
    if key == 'prices':
        p = dict(price='300', from_=True, unit_uk='/ проєкт', unit_pl='/ projekt', name_uk='Ціни на сайти', name_pl='Cennik stron',
                 tag_uk='2026', tag_pl='2026', href='prices')
    else:
        s = next(x for x in SERVICES if x['key'] == key)
        price = next((pl['price'] for pl in s['plans'] if pl.get('price')), None)
        p = dict(price=price, from_=True, unit_uk='/ проєкт', unit_pl='/ projekt', name_uk=s['name_uk'], name_pl=s['name_pl'],
                 tag_uk=s['facts'][1][2], tag_pl=s['facts'][1][3], href='svc-' + key)
    p.update(desc_uk=post['cta_uk'], desc_pl=post['cta_pl'], cta_uk='Детальніше', cta_pl='Szczegóły')
    return '''    <section class="section" id="next">
      <div class="container">
''' + head(L('Що далі', 'Co dalej'), L('Послуга', 'Usługa')) + addon(p) + '''      </div>
    </section>'''

def post_items(posts):
    return [dict(key=p['key'], img=p['img'], name_uk=p['h1_uk'], name_pl=p['h1_pl'], sub_uk=p['sub_uk'], sub_pl=p['sub_pl']) for p in posts]

def main():
    posts = load_posts()
    out = []
    for post in posts:
        others = [p for p in posts if p['key'] != post['key']][:4]
        facts = [
            ['Автор', 'Autor', 'Andrii Shestakov', 'Andrii Shestakov'],
            ['Опубліковано', 'Opublikowano', human_date(post['date'], 'uk'), human_date(post['date'], 'pl')],
            ['Читання', 'Czas czytania', f"{post['minutes']} хв", f"{post['minutes']} min"],
            ['Тема', 'Temat', post['topic_uk'], post['topic_pl']],
            ['Студія', 'Studio', 'SHSTKV Digital', 'SHSTKV Digital'],
        ]
        body = [
            hero(wm('Блог', 'Blog'), L(post['h1_uk'], post['h1_pl']), L(post['sub_uk'], post['sub_pl']), facts, 'article'),
            article(post),
            service_cta(post),
            faq_block(post['faq'], L('Питання й відповіді', 'Pytania i odpowiedzi')),
        ]
        if others:
            body.append(services_block(post_items(others), L('Читайте також', 'Przeczytaj też'), L('Блог', 'Blog'), 'post-', L('Читати', 'Czytaj')))
        body.append(CONTACT)
        write('post-' + post['key'], body)
        out.append({k: post[k] for k in ('key', 'path_uk', 'path_pl', 'h1_uk', 'h1_pl', 'title_uk', 'title_pl', 'desc_uk', 'desc_pl', 'img', 'date')}
                   | {'modified': post.get('modified', post['date'])})

    topics = []
    for p in posts:
        if (p['topic_uk'], p['topic_pl']) not in topics:
            topics.append((p['topic_uk'], p['topic_pl']))
    facts = [
        ['Статей', 'Artykułów', str(len(posts)), str(len(posts))],
        ['Мови', 'Języki', 'UA · PL', 'PL · UA'],
        ['Автор', 'Autor', 'Andrii Shestakov', 'Andrii Shestakov'],
        ['Теми', 'Tematy', ' · '.join(t[0] for t in topics[:3]), ' · '.join(t[1] for t in topics[:3])],
        ['Оновлено', 'Aktualizacja', human_date(posts[0]['date'], 'uk'), human_date(posts[0]['date'], 'pl')],
    ]
    write('blog', [
        hero(wm('Блог', 'Blog'), L('Блог про сайти, SEO і продажі онлайн', 'Blog o stronach internetowych, SEO i sprzedaży online'),
             L('Практично й без води: ціни, платформи, Google і досвід наших проєктів.', 'Konkretnie i bez lania wody: ceny, platformy, Google i doświadczenia z projektów.'),
             facts, 'posts'),
        services_block(post_items(posts), L('Статті', 'Artykuły'), L('Блог', 'Blog'), 'post-', L('Читати', 'Czytaj')).replace('id="services"', 'id="posts"'),
        CONTACT,
    ])
    json.dump({'posts': out}, open(os.path.join(HERE, '..', 'src', 'lib', 'blog.json'), 'w'), ensure_ascii=False, indent=1)
    print('built blog +', len(posts), 'posts')


if __name__ == '__main__':
    main()
