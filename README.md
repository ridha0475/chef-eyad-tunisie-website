# Chef Eyad Tunisie — site web du restaurant

Site vitrine du restaurant Chef Eyad Tunisia (Berges du Lac 2, Tunis).
Référence de structure : https://chefeyad.com.sa/ (inspiration, pas copie).

> Statut : **phase de cadrage**. Aucun code définitif avant validation des bases ci-dessous.
> `index.html` actuel = maquette provisoire en français, à remplacer.

## Décisions

| Sujet | Choix |
|---|---|
| Langues | Français (défaut), arabe, anglais |
| URL | `/fr/`, `/ar/`, `/en/` — une adresse par langue |
| Arabe | Arabe standard simple, mise en page RTL (`dir="rtl"`) |
| Traductions | Rédigées à partir du français, **relues et validées par le client** avant publication |
| Contenu | Un fichier de textes par langue (`fr.json`, `ar.json`, `en.json`), séparé de la mise en page |
| Technique | Site statique, sans framework ; un petit script génère les 3 versions depuis un modèle |
| Hébergement | GitHub Pages |

## Plan des pages

1. **Accueil** — accroche, 3 points clés, aperçu des viandes, galerie, bouton Réserver
2. **À propos** — la marque, le concept (fumage lent, vente au poids), le restaurant de Tunis
3. **Menu**
   - Viandes fumées — épaule d'agneau, jarret d'agneau, côtes de bœuf (vendues au poids : 1 kg, ½ kg, ¼ kg)
   - Accompagnements — 5 salades et riz, inclus avec la viande
   - Sauces — plus de 15 sauces maison
   - Boissons et desserts — *à confirmer avec le client (existent-ils ?)*
   - *À confirmer avec le client (rubriques présentes sur le site saoudien, absentes des sources tunisiennes) :* Salades et entrées détaillées, Burgers, Poulet, Desserts, Boissons chaudes
   - *Phase 2, à confirmer :* Offres (formules déjeuner, offres 2 ou 4 personnes)
4. **Événements et salons privés** — salon VIP, traiteur / catering
5. **Réservation** — formulaire (date, heure, convives) + lien WhatsApp
6. **Contact et accès** — adresse, téléphone, horaires, plan Google Maps ; FAQ courte *à confirmer*

Navigation fixe : bouton **Réserver** et sélecteur de langue toujours visibles.

## Phases

| Phase | Contenu |
|---|---|
| 1. Vitrine | Les 6 pages ci-dessus, en 3 langues |
| 2. Réservation et galerie | Réservation en ligne, galerie photos, actualités/offres |
| 3. Commande et livraison | Panier, paiement tunisien, livraison — **à cadrer séparément avec le client avant chiffrage** |

## Données manquantes (à obtenir du client)

- [ ] Horaires d'ouverture officiels
- [ ] Carte complète avec prix en TND (aucun prix public à ce jour)
- [ ] Photos des plats et du restaurant
- [ ] Boissons et desserts : proposés ou non
- [ ] Compte Instagram officiel (handle)
- [ ] État du domaine `chefeyad.com.tn` (erreur 526 constatée le 28/07/2026) et nom de domaine à utiliser

## Règle de contenu

Aucune information (prix, horaires, chiffres) n'est publiée sans source ou validation du client.
Ce qui manque s'affiche « à venir » ou « à confirmer ».

## Prochaines étapes

1. Rédiger le contenu français de chaque page
2. Traduire en arabe et en anglais, validation client
3. Coder le modèle et le script de génération
4. Publier sur GitHub Pages
