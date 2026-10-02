# Chef Eyad Tunisie — site web du restaurant

Site vitrine du restaurant Chef Eyad Tunisia (Berges du Lac 2, Tunis).
Référence de structure : https://chefeyad.com.sa/ (inspiration, pas copie).

> Statut : **phase de cadrage**. Aucun code définitif avant validation des bases ci-dessous.

## Décisions

| Sujet | Choix |
|---|---|
| Langues | Français (défaut), arabe, anglais |
| URL | `/fr/`, `/ar/`, `/en/` — une adresse par langue |
| Arabe | Arabe standard simple, mise en page RTL (`dir="rtl"`) |
| Traductions | Rédigées à partir du français, **relues et validées par le client** avant publication |
| Contenu | Un seul fichier `i18n.json` : chaque texte porte ses 3 langues côte à côte (relecture client facilitée), séparé de la mise en page |
| Technique | Site statique, sans framework ; un petit script génère les 3 versions depuis un modèle |
| Hébergement | GitHub Pages |

## Plan des pages

1. **Accueil** — accroche, 3 points clés, aperçu des viandes, galerie, bouton Réserver
2. **À propos** — la marque, le concept (fumage lent, vente au poids), le restaurant de Tunis
   - Histoire de la marque reprise de https://chefeyad.com.sa/ (accueil et /about-us/, 02/10/2026) : voyage du Chef Eyad dans les fumoirs du Texas, touche orientale, mélange d'épices secret, restaurants à Riyad et Al Khobar
   - *À faire valider par le client :* ce récit et le lien de franchise avec la marque saoudienne (le site saoudien annonce « jusqu'à 14 h » de fumage ; on garde 10 à 12 h, la durée de la carte de Tunis)
3. **Menu** — source : carte imprimée du restaurant (`photos-source/menu-p1-viandes.jpeg`, `menu-p2-plats.jpeg`) et prix au poids donné par le client le 02/10/2026
   - Viandes fumées (8 plats, riz basmati et 5 salades à volonté) · Au poids (veau et agneau, 27,900 DT / 100 g) · Pâtes Chef Eyad · Poutines & frites · Tasty Smoky · Sauces
   - *À confirmer avec le client :* boissons, desserts, détail des sauces ; mention « bacon » (préciser bœuf ou dinde, restaurant halal)
4. **Événementiel et salon VIP** — Chef Eyad se déplace dans le Grand Tunis (mariages, fiançailles, anniversaires, fêtes de famille et d'entreprise) : viande livrée prête, découpe sur place devant les invités (client, 02/10/2026) ; salon VIP au restaurant ; demande de devis sur WhatsApp
5. **Réservation** — formulaire en 3 étapes (convives, date et heure de 12:00 à 23:30, coordonnées), résumé en direct, envoi WhatsApp dans la langue de la page
6. **Contact et accès** — adresse, téléphone, WhatsApp, horaires avec état ouvert/fermé, plan Google Maps intégré (fiche « Chef Eyad Tunisia », Regency 3) ; FAQ courte *à confirmer, non publiée*

Navigation fixe : bouton **Réserver** et sélecteur de langue toujours visibles.

## Fabriquer le site

```bash
python3 build.py      # lit i18n.json + templates/, écrit docs/{fr,ar,en}/*.html
```

- Textes : `i18n.json` · mise en page : `templates/*.html` et `style.css` · **ne jamais éditer `docs/` à la main** (écrasé à chaque génération).
- La réservation ouvre WhatsApp avec la demande pré-remplie (pas de serveur).
- Test local : `cd docs && python3 -m http.server 8000` puis http://localhost:8000
- Publication : GitHub Pages, branche `main`, dossier `/docs`.

## Phases

| Phase | Contenu |
|---|---|
| 1. Vitrine | Les 6 pages ci-dessus, en 3 langues |
| 2. Réservation et galerie | Réservation en ligne, galerie photos, actualités/offres |
| 3. Commande et livraison | Panier, paiement tunisien, livraison — **à cadrer séparément avec le client avant chiffrage** |

## Données manquantes (à obtenir du client)

- [x] Horaires d'ouverture : tous les jours, 12 h – minuit (client, 02/10/2026) ; pas de taille maximale de groupe
- [x] Carte avec prix en TND (carte imprimée, 02/10/2026)
- [ ] Photos des plats et du restaurant
- [ ] Boissons et desserts : absents de la carte imprimée, proposés ou non ?
- [ ] Compte Instagram officiel (handle)
- [ ] État du domaine `chefeyad.com.tn` (erreur 526 constatée le 28/07/2026) et nom de domaine à utiliser

## Photos

- Sources autorisées : photos des comptes Facebook/Instagram du restaurant (propriété du client), originaux fournis par le client, séance photo.
- Exclues : Google Images, photos d'autres branches, photos de tiers repostées (clients, influenceurs, franchiseur) sans accord écrit.
- Idéal : originaux haute définition plutôt que des téléchargements des réseaux sociaux.
- Dépôt des sources : `photos-source/` ; les versions optimisées du site iront dans `images/`.
- `images/menu-feu.webp` (en-tête de la page Menu) est découpée dans la carte imprimée du client (827 px de large, un peu juste en grand écran : demander l'original HD).
- **Exception provisoire** : `images/fumoir.webp`, `images/vente-au-poids.webp`, `images/accompagnements.webp` et `images/sauces.webp` (chapitres 01 à 04) sont des images générées par IA, en attendant de vraies photos. À faire valider par le client ou à remplacer avant publication.

## Règle de contenu

Aucune information (prix, horaires, chiffres) n'est publiée sans source ou validation du client.
Ce qui manque s'affiche « à venir » ou « à confirmer ».

## Prochaines étapes

1. Rédiger le contenu français de chaque page
2. Traduire en arabe et en anglais, validation client
3. Coder le modèle et le script de génération
4. Publier sur GitHub Pages
