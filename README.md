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
| Hébergement | GitHub Pages, actif depuis le 02/10/2026 : https://ridha0475.github.io/chef-eyad-tunisie-website/ |

## Plan des pages

1. **Accueil** — accroche, 3 points clés, aperçu des viandes, galerie, bouton Réserver
2. **À propos** — la marque, le concept (fumage lent, vente au poids), le restaurant de Tunis
   - Histoire de la marque reprise de https://chefeyad.com.sa/ (accueil et /about-us/, 02/10/2026) : voyage du Chef Eyad dans les fumoirs du Texas, touche orientale, mélange d'épices secret, restaurants à Riyad et Al Khobar
   - Textes arabes de la page corrigés par le client (07/10/2026). **Franchise : Chef Eyad Tunisie fait partie du réseau international, sous licence de la maison mère** (client, 07/10/2026) ; réseau présent en Palestine, Turquie, Jordanie, Irak et dans le Golfe (sources : chefeyad.net). **Ne jamais citer Kafr Qasim** (ville d'Israël, mal vu en Tunisie ; décision de l'utilisateur, 07/10/2026). Pas de chiffre (nombre de pays ou de restaurants) sans validation du client.
3. **Menu** — source : carte imprimée du restaurant (`photos-source/menu-p1-viandes.jpeg`, `menu-p2-plats.jpeg`) et prix au poids donné par le client le 02/10/2026
   - Viandes fumées (8 plats, riz basmati et 5 salades à volonté) · Au poids (veau et agneau, 27,900 DT / 100 g) · Pâtes Chef Eyad · Poutines & frites · Tasty Smoky · Sauces
   - Sauces : **3 sauces maison, qui changent selon les saisons** (client, 02/10/2026) — ne plus écrire « 15 sauces »
   - Boissons (client, 07/10/2026) : boisson gazeuse, eau minérale 1 L / 1,5 L / 2 L, citronnade, citronnade menthe, café, café turc (10 DT), thé kufi (orthographe et nom arabe à confirmer)
   - *À confirmer avec le client :* desserts ; mention « bacon » (préciser bœuf ou dinde, restaurant halal)
4. **Événementiel et salon VIP** — Chef Eyad se déplace dans le Grand Tunis (mariages, fiançailles, anniversaires, fêtes de famille et d'entreprise) : viande livrée prête, découpe sur place devant les invités (client, 02/10/2026) ; salon VIP au restaurant (groupes de 25 à 40 personnes, privatisation 399 DT, client 07/10/2026) ; demande de devis sur WhatsApp
5. **Réservation** — formulaire en 3 étapes (convives, date et heure de 12:00 à 23:30, coordonnées), résumé en direct, envoi WhatsApp dans la langue de la page
6. **Contact et accès** — adresse, téléphone, WhatsApp, horaires avec état ouvert/fermé, plan Google Maps (fiche « Chef Eyad Tunisia », Regency 3) chargé seulement au clic sur « Afficher le plan » ; FAQ courte *à confirmer, non publiée*

7. **Mentions légales et confidentialité** (`privacy.html`, deux liens dans le pied de page vers `#legal` et `#privacy`, hors menu) — structure inspirée des sites BIAT, Orange Tunisie, STB et Attijari bank. *Mentions légales* : éditeur, hébergeur, informations et prix (seuls ceux du restaurant font foi), liens externes, propriété intellectuelle, droit tunisien et tribunaux de Tunis. *Politique de confidentialité* : données des formulaires, journaux du serveur, cookies, droits (loi organique n° 2004-63, INPDP) ; préparée le 07/10/2026, **à faire relire par un juriste**

Navigation fixe : bouton **Réserver** et sélecteur de langue toujours visibles.

## Confidentialité (décidé le 07/10/2026)

- **Aucun cookie, donc pas de bandeau** : pas de statistiques, pas de stockage navigateur ; polices hébergées dans `fonts/` (tirées de Google Fonts, sous-ensembles latin et arabe) ; plan Google Maps chargé seulement au clic.
- Ne rien ajouter qui dépose un cookie ou appelle un tiers au chargement (statistiques, pixel Meta, widget, vidéo YouTube intégrée) sans revoir la page Confidentialité et prévoir un consentement.
- Hébergement définitif : **VPS OVH**. La page l'annonce déjà ; GitHub Pages n'est qu'une préproduction.
- **Veille juridique** (07/10/2026) : l'INPDP existe toujours (loi 2004-63 en vigueur), mais le mandat de son conseil a expiré en avril 2024 et son site inpdp.tn ne répond plus. La proposition de loi organique n° 095/2025 (déposée le 14/07/2025, en commission des droits et libertés) la remplacerait par une « هيئة حماية المعطيات الشخصية » (Autorité de protection des données personnelles). Si elle est adoptée, revoir la page Confidentialité (nom de l'autorité, loi citée, déclaration préalable).
- Engagements pris dans la page, à respecter sur le serveur : journaux Nginx gardés **12 mois au plus** (logrotate), réponse aux demandes sous un mois.

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

## Backend (à faire plus tard — décidé le 02/10/2026)

Besoins retenus : réservations et devis enregistrés, contenu modifiable par le client, notifications, commande en ligne. Hébergement : **notre propre serveur** (VPS).

Architecture proposée : **Django** (admin intégré = tableau de bord + édition du contenu en fr/ar/en), SQLite puis PostgreSQL, Nginx, HTTPS Let's Encrypt. Le site public reprend les mêmes modèles et le même design ; GitHub Pages devient préproduction ou est coupé.

1. Socle Django + reprise des 6 pages + réservations et devis enregistrés, tableau de bord (confirmer / refuser / planning du jour). WhatsApp reste en option.
2. Contenu modifiable : carte, prix, horaires, photos, textes.
3. Notifications : e-mail au restaurant, confirmation e-mail ou SMS au client ; WhatsApp Business API (Meta) plus tard.
4. Commande en ligne : panier, paiement tunisien (Konnect, Paymee, Flouci ou ClicToPay), livraison — **cadrage client d'abord**.

À obtenir avant de démarrer : serveur (fournisseur), nom de domaine (chefeyad.com.tn en erreur 526, qui y a accès ?), adresse e-mail de réception des demandes ; pour la commande : livraison ou retrait, zone et frais, prestataire de paiement, plats commandables (viande au poids).

## Données manquantes (à obtenir du client)

- [x] Horaires d'ouverture : tous les jours, 12 h – minuit (client, 02/10/2026) ; pas de taille maximale de groupe
- [x] Carte avec prix en TND (carte imprimée, 02/10/2026)
- [x] Photos des plats et du restaurant (photothèque Drive, 02/10/2026)
- [x] Boissons : liste et prix donnés par le client (07/10/2026), section 07 de la carte
- [ ] Desserts : proposés ou non ?
- [ ] Compte Instagram officiel (handle)
- [ ] État du domaine `chefeyad.com.tn` (erreur 526 constatée le 28/07/2026) et nom de domaine à utiliser
- [x] Société : SARL « Panorient », matricule fiscal et siège (carte d'identification fiscale, 07/10/2026) → `documents-client/societe.md`, **non versionné**
- [x] E-mail pour les demandes sur les données personnelles : hr@panorient.tn (07/10/2026)
- [x] Responsable de la publication : Nassim Mami, gérant (07/10/2026)
- [x] Identifiant unique RNE : 1819200/L (07/10/2026)
- Capital social : pas affiché, décision de l'utilisateur (07/10/2026)
- [ ] Déclaration à l'INPDP faite ou non (obligatoire avant de traiter des données personnelles), et son numéro — **à vérifier** (téléphone INPDP 71 799 853) ; ligne retirée de la page en attendant, clé `privacy.k_inpdp` gardée pour la remettre avec le numéro
- [x] Durée de conservation des demandes WhatsApp : 12 mois au plus (validé le 07/10/2026)

## Photos

- Sources autorisées : photos des comptes Facebook/Instagram du restaurant (propriété du client), originaux fournis par le client, séance photo.
- Exclues : Google Images, photos d'autres branches, photos de tiers repostées (clients, influenceurs, franchiseur) sans accord écrit.
- **Photothèque du client** (reçue le 02/10/2026, Drive https://drive.google.com/drive/folders/1aUsyKUt9Qy9bduarwUMVwYwm3GLQE6EN) : 418 photos uniques rangées dans `photos-client/` par thème (`plats/`, `ambiance/`, `equipe/`, `identite/`, `affiches/`, `divers/`), nommées `<theme>/<sujet>-NN.jpg`. `photos-client/INDEX.csv` relie chaque fichier à son nom et son identifiant d'origine sur le Drive. Le dossier pèse 2,6 Go : **il n'est pas versionné** (seul l'index l'est) ; pour le reconstituer, retélécharger depuis le Drive avec l'index. Les 95 vidéos (5,6 Go, surtout des préparations de plateaux traiteur : poisson, poulets farcis, agneau entier sur riz, découpe) sont dans `photos-client/videos/`, nommées par sujet ; index `photos-client/INDEX-VIDEOS.csv`.
  - À ne pas publier : `divers/stand-autre-marque-01.jpg` (autre marque), les affiches avec d'anciens prix, les poutines à viande rose (aspect charcuterie, restaurant halal).
  - `ambiance/` et `equipe/` viennent surtout du shooting pro avant ouverture (haute définition) ; les fichiers d'origine `IMG-…-WA…` sont des photos WhatsApp, en basse définition.
- Photos du site (`images/`, toutes issues de `photos-client/`, recadrées et converties en WebP qualité 80) : `agneau-sauces` (hero accueil) ← `plats/agneau-plateau-05` · `fumoir` ← `ambiance/fumoir-01` · `viande-gants` ← `plats/viande-gants-01` · `agneau-accompagnements` ← `plats/agneau-plateau-06` · `sauces` ← `plats/viande-effilochee-09` · `flammes-chef` (Menu) ← `ambiance/flammes-03` · `viande-flambee` (À propos) ← `plats/viande-flambee-08` · `chef-decoupe` ← `equipe/chef-decoupe-02` · `service-foule` (Événementiel, photo WhatsApp basse déf.) ← `equipe/service-foule-02` · `salle` (salon VIP, à confirmer que c'est bien le salon) ← `ambiance/salle-02`.
- **Archivées** (plus utilisées) : `archives/ia/` (4 images générées par IA, chapitres de l'accueil) et `archives/internet/` (`short-ribs`, photo de banque d'images de l'ancien hero, droits jamais confirmés).

## Règle de contenu

Aucune information (prix, horaires, chiffres) n'est publiée sans source ou validation du client.
Ce qui manque s'affiche « à venir » ou « à confirmer ».

## Prochaines étapes

1. Rédiger le contenu français de chaque page
2. Traduire en arabe et en anglais, validation client
3. Coder le modèle et le script de génération
4. Publier sur GitHub Pages
