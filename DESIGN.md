# Design system — Chef Eyad Tunisie

Référence visuelle du site. **`style.css` reste la source technique** : ce document explique ses choix et fixe les règles. Toute nouvelle page part d'ici ; si un choix change, on met à jour les deux.

## 1. Direction

**Le feu, la fumée, la patience.** Un site sombre comme un fumoir, éclairé par la braise et l'or du logo. On raconte le fumage lent comme un récit en chapitres, avec une intensité qui monte jusqu'à l'appel à réserver.

- Ambiance : chaleureuse, haut de gamme, généreuse. Pas froide, pas « luxe de bijouterie ».
- Mode : sombre uniquement (pas de thème clair).
- Ce qu'on évite : gabarits de restaurant standard, cartes génériques en grille, effets de verre, couleurs « tech » (bleus, violets), images qui évoquent le porc ou l'alcool (restaurant halal).

## 2. Couleurs

| Jeton | Valeur | Rôle |
|---|---|---|
| `--bg` | `#0e0a08` | Fond de page (charbon) |
| `--bg2` | `#161009` | Fond secondaire |
| `--card` | `#1c1512` | Cartes, champs de formulaire, menus déroulants |
| `--line` | `#2c211b` | Filets et bordures |
| `--txt` | `#f6ede2` | Texte principal (crème) |
| `--mute` | `#c4b4a5` | Texte secondaire |
| `--fire` | `#e8561c` | Braise : bouton principal, dégradés du final |
| `--fire2` | `#ff7a35` | Braise vive : survol, particules |
| `--gold` | `#e9b44c` | Or du logo : surtitres, titres de section, focus, liens |

Contrastes mesurés (WCAG) :

| Couple | Ratio | Usage permis |
|---|---|---|
| `--txt` sur `--bg` | 17,0 | Tout texte |
| `--mute` sur `--bg` / `--card` | 9,8 / 8,9 | Tout texte |
| `--gold` sur `--bg` / `--card` | 10,4 / 9,5 | Tout texte |
| blanc sur `--fire` | 3,6 | Texte ≥ 19 px gras seulement |
| blanc sur `--fire2` | **2,6** | Aucun texte |
| `--bg` sur `--fire` / `--fire2` | 5,4 / 7,6 | Tout texte — utilisé pour le bouton `.btn` |

Règles :
- Pas de couleur en dur dans les composants : passer par les jetons (les transparences du type `#0e0a08cc` sont des variantes de `--bg`).
- L'or sert à guider l'œil (petits textes, titres) ; la braise est réservée à l'action (réserver) et au final.
- L'intensité de couleur monte avec le défilement : chapitres 1 → 4 de plus en plus rougeoyants, final en plein feu.

## 3. Typographie

| Rôle | Latin (fr, en) | Arabe |
|---|---|---|
| Titres `--f-display` | Cormorant 600–700 | Noto Naskh Arabic |
| Texte `--f-body` | Montserrat 400–600 | Noto Sans Arabic |

| Élément | Taille |
|---|---|
| Titre du hero | `clamp(2.8rem, 8vw, 6.2rem)`, max 12 caractères de large (14 en arabe) |
| `h1` | 2,6rem |
| `h2` de chapitre | `clamp(2rem, 4.5vw, 3.4rem)` |
| `h2` courant | 1,8rem, or |
| Texte | 16 px, interligne 1,7 |
| Surtitre `.eyebrow` | 0,78rem, majuscules, espacement 0,22em, or |
| Grand numéro `.num` | `clamp(5rem, 13vw, 10rem)`, contour or, fond transparent |

Polices hébergées sur le site (`fonts/latin.css`, `fonts/ar.css`), jamais chargées depuis Google.

Règles :
- Jamais de texte courant sous 14 px.
- **Arabe** : pas de majuscules ni d'espacement entre lettres (ça casse les liaisons) ; surtitres à 0,95rem ; interligne des grands titres 1,35.
- Longueur de ligne : 46 à 65 caractères pour les paragraphes.

## 4. Espacement et mise en page

- Conteneur `.w` : 1 120 px max, marges latérales 20 px ; `.narrow` : 640 px pour les textes longs.
- Rythme vertical : sections 64 px ; chapitres 72 px (52 px sur mobile) ; final 120 px. Le site respire : préférer plus d'espace à plus de contenu.
- Rayon `--r` : 14 px (cartes, photos) ; boutons et étiquettes en pilule (99 px) ; champs 10 px.
- Point de rupture unique : **760 px**. En dessous, tout passe en une colonne.
- **RTL** : utiliser les propriétés logiques (`inset-inline-start`, `padding-inline`…) plutôt que `left`/`right`. Quand ce n'est pas possible (dégradés, `transform-origin`), ajouter la variante `[dir=rtl]`.

## 5. Composants

| Composant | Classe | Notes |
|---|---|---|
| Bouton principal | `.btn` | Braise, texte charbon, pilule, hauteur min 44 px. Un seul par écran, toujours pour réserver. |
| Bouton secondaire | `.btn.o` | Contour clair transparent. |
| Bouton sur fond braise | `.btn.light` | Crème sur rouge, pour le final. |
| Lien d'action | `.link` | Or, souligné au survol. |
| En-tête | `.nav` | Collant ; transparent sur l'accueil, opaque flouté après défilement. Bouton Réserver et langues toujours visibles. |
| Chapitre | `.ch` + `.num` | Numéro géant en contour, titre, texte ; variantes `.has-img` (photo) et `.flip` (photo à gauche). |
| Carte | `.c` | Pour les autres pages ; à remplacer progressivement par des mises en page moins « grille de cartes ». |
| Étiquette | `.tag` | Contour or, ex. « à confirmer ». |
| Carte à prix | `.mc` + `.ml` | Section du menu : titre collant à gauche, liste nom · pointillés · prix (or). Description en dessous, en gris. |
| Barre de catégories | `.mnav` | Collée sous l'en-tête, une seule ligne qui défile au doigt ; catégorie en cours en or plein (`aria-current`). Liens d'ancre, fonctionne sans JS. |
| Ligne de fumage | `.tl` + `.st` | Page À propos : ligne verticale graduée 00:00 → 12:00, la braise la remplit au défilement et allume chaque étape (`.on`) aux 3/5 de l'écran. Sans JS ou en mouvement réduit : ligne pleine, étapes allumées. |
| Villes de la marque | `.route` | Noms en grand Cormorant reliés par un filet ; Tunis en braise vive. En colonne sur mobile. |
| Formulaire de réservation | `.bform` + `.chip` + `.bside` | Étapes numérotées (`legend .n`), convives en pastilles rondes (braise quand choisi), « 8+ » ouvre un champ libre en CSS (`:has`). Résumé or en direct au-dessus du bouton. Infos collantes à côté, sous le formulaire sur mobile. |
| Bandeau des occasions | `.occ` | Page Événementiel : occasions en grand qui défilent en boucle (40 s), une sur deux en or, séparées par ✦ braise. Liste doublée en `aria-hidden` ; en mouvement réduit, liste fixe sur plusieurs lignes. |
| Pastilles de texte | `.chip.txt` | Variante des pastilles de convives pour des choix en mots (type d'événement). |
| Coordonnées | `.cont-in` + `.cl` + `.now` | Page Contact : plan Google assombri par filtre CSS (ton charbon) à côté de la liste des coordonnées ; téléphone en grand Cormorant ; pastille « Ouvert en ce moment » calculée à l'heure de Tunis. Sur mobile, coordonnées avant le plan. |
| Infos pratiques | `.visit` | Bandeau adresse / horaires / contact. |
| Plan au clic | `.map-load` | Lien vers Google Maps qui, avec JS, remplace l'encart par le plan intégré ; bouton `.btn.o` et note sur les cookies. Sans JS, ouvre Google Maps. |
| Texte légal | `.legal` + `.kv` | Page Confidentialité : colonne `.narrow`, titres or, tableau clé / valeur pour l'éditeur (une colonne sur mobile), étiquettes `.tag` pour ce qui reste à confirmer. |

## 6. Photos

- Ratio : 4/5 (portrait) dans les chapitres, 4/3 (`.wide`) ou en mobile ; hero en plein écran.
- Format WebP, ombre portée profonde (`0 30px 80px #0009`), dégradé sombre par-dessus le hero pour la lisibilité du texte.
- Tons chauds, fumée, braise, viande cuite ; jamais de porc, d'alcool ou de charcuterie ambiguë.
- Origine : photothèque du client (`photos-client/`), voir le README. Plus aucune image IA ni de banque d'images.

## 7. Mouvement

| Effet | Durée | Courbe |
|---|---|---|
| Survol (couleur, bouton) | 200 ms | `ease` |
| Apparition au défilement `.reveal` | 700 ms, décalage 14 px | `--ease` = `cubic-bezier(.2,.7,.2,1)` |
| Zoom lent du hero | 18 s | `--ease` |
| Braises qui montent | 9–13 s, en boucle | linéaire |
| Barre de progression | liée au défilement | — |

Règles :
- CSS uniquement, pas de bibliothèque d'animation.
- On n'anime que `opacity` et `transform`.
- Le contenu doit être lisible sans JavaScript (`.reveal` n'est masqué que si la classe `js-reveal` est posée).
- `prefers-reduced-motion` : toutes les animations coupées, braises et barre masquées.

## 8. Accessibilité (minimum non négociable)

- Contraste 4,5:1 pour le texte (voir tableau des couleurs).
- Focus visible : contour or 2 px, jamais supprimé.
- Cibles tactiles ≥ 44 × 44 px.
- `alt` sur toutes les photos de contenu ; `lang` et `dir` sur chaque page.
- Formulaires : libellé visible au-dessus de chaque champ, pas de placeholder seul.

## 9. Points ouverts

- [ ] Menu déroulant `.dd` masqué sur mobile : les sous-pages doivent rester accessibles autrement.
- [x] Direction appliquée aux 6 pages.
