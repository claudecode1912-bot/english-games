# -*- coding: utf-8 -*-
"""Генерирует озвучку для игр english-games (A Rainy Saturday, Feed Tops) тем же голосом, что и учебник «Читаю по-английски».
Запуск: двойной щелчок по make_audio.bat (или: python make_audio.py [голос])."""
import asyncio, json, os, sys, subprocess

try:
    import edge_tts
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "edge-tts"])
    import edge_tts

VOICE = sys.argv[1] if len(sys.argv) > 1 else "en-GB-SoniaNeural"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "games-audio")
os.makedirs(OUT, exist_ok=True)
ITEMS = json.loads('[["be-was-or-were-been-z2dfox", "be, was or were, been", "word"], ["have-had-had-1bdas6p", "have, had, had", "word"], ["do-did-done-u8sy7d", "do, did, done", "word"], ["go-went-gone-11ixweq", "go, went, gone", "word"], ["come-came-come-c1agqr", "come, came, come", "word"], ["see-saw-seen-10q7rnm", "see, saw, seen", "word"], ["get-got-got-13fbv3r", "get, got, got", "word"], ["make-made-made-fwljav", "make, made, made", "word"], ["take-took-taken-189m7m0", "take, took, taken", "word"], ["give-gave-given-1evrc9y", "give, gave, given", "word"], ["say-said-said-1d0molw", "say, said, said", "word"], ["eat-ate-eaten-bxgej0", "eat, ate, eaten", "word"], ["drink-drank-drunk-uul7yt", "drink, drank, drunk", "word"], ["run-ran-run-1jt8c7c", "run, ran, run", "word"], ["sit-sat-sat-1xasyvf", "sit, sat, sat", "word"], ["sleep-slept-slept-1ck1ihg", "sleep, slept, slept", "word"], ["read-read-read-3nk6jp", "read, read, read", "word"], ["write-wrote-written-15hsv6o", "write, wrote, written", "word"], ["swim-swam-swum-5hmu01", "swim, swam, swum", "word"], ["sing-sang-sung-1oztyge", "sing, sang, sung", "word"], ["buy-bought-bought-1tyt1s3", "buy, bought, bought", "word"], ["bring-brought-brought-1nhv005", "bring, brought, brought", "word"], ["think-thought-thought-11734dt", "think, thought, thought", "word"], ["teach-taught-taught-1e257t2", "teach, taught, taught", "word"], ["catch-caught-caught-dnqabg", "catch, caught, caught", "word"], ["fly-flew-flown-r9bfl6", "fly, flew, flown", "word"], ["draw-drew-drawn-1cdz9vb", "draw, drew, drawn", "word"], ["know-knew-known-x1dscq", "know, knew, known", "word"], ["grow-grew-grown-datkze", "grow, grew, grown", "word"], ["throw-threw-thrown-b30w1h", "throw, threw, thrown", "word"], ["break-broke-broken-14nmxas", "break, broke, broken", "word"], ["speak-spoke-spoken-x2qpw1", "speak, spoke, spoken", "word"], ["begin-began-begun-1fh0w0o", "begin, began, begun", "word"], ["ride-rode-ridden-15menfh", "ride, rode, ridden", "word"], ["drive-drove-driven-1hhvmet", "drive, drove, driven", "word"], ["find-found-found-1071a7e", "find, found, found", "word"], ["tell-told-told-1r783ya", "tell, told, told", "word"], ["sell-sold-sold-xp4qr5", "sell, sold, sold", "word"], ["leave-left-left-t207ck", "leave, left, left", "word"], ["meet-met-met-almfiu", "meet, met, met", "word"], ["fall-fell-fallen-rtgj3n", "fall, fell, fallen", "word"], ["feel-felt-felt-diajht", "feel, felt, felt", "word"], ["forget-forgot-forgotten-xanrv", "forget, forgot, forgotten", "word"], ["choose-chose-chosen-2cbi6q", "choose, chose, chosen", "word"], ["hide-hid-hidden-1ubscju", "hide, hid, hidden", "word"], ["bite-bit-bitten-17cou8k", "bite, bit, bitten", "word"], ["wear-wore-worn-3ncqkn", "wear, wore, worn", "word"], ["steal-stole-stolen-1uxbxdk", "steal, stole, stolen", "word"], ["freeze-froze-frozen-qylrpw", "freeze, froze, frozen", "word"], ["shake-shook-shaken-xrgy0x", "shake, shook, shaken", "word"], ["lose-lost-lost-1fwzidg", "lose, lost, lost", "word"], ["build-built-built-htem8n", "build, built, built", "word"], ["send-sent-sent-clljtn", "send, sent, sent", "word"], ["spend-spent-spent-lpgjzv", "spend, spent, spent", "word"], ["keep-kept-kept-dqwuoo", "keep, kept, kept", "word"], ["dig-dug-dug-15hfe0v", "dig, dug, dug", "word"], ["hold-held-held-y94kxs", "hold, held, held", "word"], ["understand-understood-understood-rh5doj", "understand, understood, understood", "word"], ["learn-learnt-or-learned-learnt-or-learne-jjgxvx", "learn, learnt or learned, learnt or learned", "word"], ["dream-dreamt-or-dreamed-dreamt-or-dreame-vali2k", "dream, dreamt or dreamed, dreamt or dreamed", "word"], ["hear-heard-heard-igpjj5", "hear, heard, heard", "word"], ["show-showed-shown-1kr6u35", "show, showed, shown", "word"], ["stand-stood-stood-1inhw7p", "stand, stood, stood", "word"], ["put-put-put-13dt95s", "put, put, put", "word"], ["cut-cut-cut-1alts33", "cut, cut, cut", "word"], ["let-let-let-1dvvsrw", "let, let, let", "word"], ["pay-paid-paid-adnth9", "pay, paid, paid", "word"], ["win-won-won-hvenh1", "win, won, won", "word"], ["fight-fought-fought-7ibn5l", "fight, fought, fought", "word"], ["feed-fed-fed-1izc1n7", "feed, fed, fed", "word"], ["wake-woke-woken-3pr6gp", "wake, woke, woken", "word"], ["ring-rang-rung-6luw7z", "ring, rang, rung", "word"], ["shut-shut-shut-1smdlsf", "shut, shut, shut", "word"], ["hit-hit-hit-1083nw4", "hit, hit, hit", "word"], ["cost-cost-cost-11qr0b4", "cost, cost, cost", "word"], ["burn-burnt-or-burned-burnt-or-burned-9ehfyw", "burn, burnt or burned, burnt or burned", "word"], ["blow-blew-blown-101e7uv", "blow, blew, blown", "word"], ["become-became-become-1lsawom", "become, became, become", "word"], ["mean-meant-meant-rjfoam", "mean, meant, meant", "word"], ["lend-lent-lent-dwfr9o", "lend, lent, lent", "word"], ["sweep-swept-swept-1cl3hkl", "sweep, swept, swept", "word"], ["swing-swung-swung-1qwai29", "swing, swung, swung", "word"], ["shine-shone-shone-1yysw0m", "shine, shone, shone", "word"], ["tear-tore-torn-39ht3c", "tear, tore, torn", "word"], ["beat-beat-beaten-1w29lu2", "beat, beat, beaten", "word"], ["bend-bent-bent-ilngmi", "bend, bent, bent", "word"], ["bet-bet-bet-hba82", "bet, bet, bet", "word"], ["bleed-bled-bled-v89wt7", "bleed, bled, bled", "word"], ["breed-bred-bred-s6wihp", "breed, bred, bred", "word"], ["forgive-forgave-forgiven-srm71", "forgive, forgave, forgiven", "word"], ["hurt-hurt-hurt-17f79f8", "hurt, hurt, hurt", "word"], ["lay-laid-laid-1fa8329", "lay, laid, laid", "word"], ["lead-led-led-11su3j9", "lead, led, led", "word"], ["lean-leant-or-leaned-leant-or-leaned-1kyl60d", "lean, leant or leaned, leant or leaned", "word"], ["quit-quit-quit-1qge0cm", "quit, quit, quit", "word"], ["rise-rose-risen-ektmro", "rise, rose, risen", "word"], ["set-set-set-dvag7j", "set, set, set", "word"], ["shoe-shod-shod-1g6gzb6", "shoe, shod, shod", "word"], ["shoot-shot-shot-10xagy8", "shoot, shot, shot", "word"], ["shrink-shrank-shrunk-aqsqnc", "shrink, shrank, shrunk", "word"], ["sink-sank-sunk-1eqenky", "sink, sank, sunk", "word"], ["spill-spilt-or-spilled-spilt-or-spilled-15u4ugd", "spill, spilt or spilled, spilt or spilled", "word"], ["spread-spread-spread-wng3om", "spread, spread, spread", "word"], ["speed-sped-sped-5ra7p4", "speed, sped, sped", "word"], ["stick-stuck-stuck-qxuk5f", "stick, stuck, stuck", "word"], ["sting-stung-stung-v1vb8o", "sting, stung, stung", "word"], ["stink-stank-stunk-vgpw7s", "stink, stank, stunk", "word"], ["swear-swore-sworn-jfsnuk", "swear, swore, sworn", "word"], ["tips-tqq1ob", "tips", "word"], ["empty-6u9vqm", "empty", "word"], ["dirty-1847iqj", "dirty", "word"], ["clean-mbe0xq", "clean", "word"], ["neighbor-dxddm3", "neighbor", "word"], ["need-vvv65p", "need", "word"], ["bake-cnqx6o", "bake", "word"], ["pack-in-fhsxhb", "pack in", "word"], ["fix-repair-1s4xc01", "fix, repair", "word"], ["fix-repair-s2xieu", "fix / repair", "word"], ["wooden-21k2u3", "wooden", "word"], ["suitable-khkuiw", "suitable", "word"], ["stick-1smgdaf", "stick", "word"], ["our-1ax46k9", "our", "word"], ["start-s2jf1b", "start", "word"], ["at-the-same-time-7b9usc", "at the same time", "word"], ["something-z1d27f", "something", "word"], ["each-of-us-rt11sb", "each of us", "word"], ["hear-b7nksl", "hear", "word"], ["our-own-1667lal", "our own", "word"], ["clearly-1yvwl3d", "clearly", "word"], ["clear-pn999e", "clear", "word"], ["get-ready-afzy04", "get ready", "word"], ["rain-126ubwz", "rain", "word"], ["it-s-raining-pccwws", "it\'s raining", "word"], ["lead-a2fmlr", "lead", "word"], ["break-1jvnkag", "break", "word"], ["dry-1p2zqla", "dry", "word"], ["blanket-1yqy9ag", "blanket", "word"], ["this-1oj91fl", "this", "word"], ["enough-zip4ll", "enough", "word"], ["clothes-7cthcr", "clothes", "word"], ["twins-1hza000", "twins", "word"], ["brushes-1inez5v", "brushes", "word"], ["put-on-1byfhj7", "put on", "word"], ["choose-jp6mgw", "choose", "word"], ["know-ji60fe", "know", "word"], ["all-5b8o90", "all", "word"], ["enjoy-4mijak", "enjoy", "word"], ["hi-my-name-is-lily-and-this-is-my-brothe-1ihwo04", "Hi! My name is Lily, and this is my brother Tom. We are twins. Every Saturday we help our neighbor, Mrs Brown. She is old and she needs help with the house. She always gives us tips, a little money for our work. Today it\'s raining. I can hear the rain clearly on the window. \\"No problem,\\" Mrs Brown says. \\"I know something we can do inside.\\" Right now we are getting ready. Tom is putting on his old clothes, because our work is often dirty. I am choosing a suitable jumper. Not my new one! Mrs Brown has an old wooden chair. One leg is broken. Tom loves to fix things, so at the moment he is repairing the chair. He is sticking the leg back with strong glue. \\"Don\'t break it again!\\" I laugh. I am helping Mrs Brown in the kitchen. We bake cookies every Saturday, and today we are baking chocolate ones. The table is clean, but the bowls are dirty and the cookie jar is empty. We make thirty cookies. That\'s enough for each of us! Then we start a new project. Mrs Brown gives us brushes and paper, and we paint at the same time. Tom is painting a dog, and I am painting the rain. Each of us paints our own picture, and we all enjoy it. In the evening the rain stops, and the sky is clear. Biscuit, Mrs Brown\'s dog, is waiting at the door with his lead in his mouth. We take him for a walk. When we come back, Biscuit is wet, so we dry him with an old blanket. Before we go home, Mrs Brown packs the cookies in a box. \\"This is for your mum,\\" she says. We know it: Saturday is the best day of the week!", "text"]]')
RATE = {"text": "-10%", "phrase": "-10%", "question": "-10%", "word": "-5%", "letter": "-5%"}

done = 0
failed = []

async def one(sem, key, say, kind):
    global done
    path = os.path.join(OUT, key + ".mp3")
    if os.path.exists(path) and os.path.getsize(path) > 500:
        done += 1
        return
    async with sem:
        for attempt in range(4):
            try:
                tmp = path + ".part"
                await edge_tts.Communicate(say, VOICE, rate=RATE.get(kind, "-5%")).save(tmp)
                if os.path.getsize(tmp) < 500:
                    raise RuntimeError("пустой файл")
                os.replace(tmp, path)
                break
            except Exception as e:
                if attempt == 3:
                    failed.append((key, say, str(e)))
                else:
                    await asyncio.sleep(2 + attempt * 3)
    done += 1
    if done % 25 == 0 or done == len(ITEMS):
        print(f"  готово {done} из {len(ITEMS)}", flush=True)

async def main():
    print(f"Голос: {VOICE}. Файлов: {len(ITEMS)}. Это займёт 5–15 минут, окно не закрывайте.\n", flush=True)
    sem = asyncio.Semaphore(6)
    await asyncio.gather(*(one(sem, k, s, t) for k, s, t in ITEMS))
    manifest = {}
    for k, s, t in ITEMS:
        p = os.path.join(OUT, k + ".mp3")
        if os.path.exists(p) and os.path.getsize(p) > 500:
            manifest[k] = "mp3"
    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f)
    print(f"\nГотово: {len(manifest)} из {len(ITEMS)} файлов в папке audio.")
    if failed:
        print(f"Не получилось: {len(failed)}. Запустите make_audio.bat ещё раз, он доделает только недостающее.")
    else:
        print("Готово. Напишите Claude в чат: «озвучка готова».")

asyncio.run(main())
