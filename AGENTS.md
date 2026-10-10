# AGENTS.md : suivi du projet pour les IA

Ce fichier s'adresse à toute IA ou à toute personne qui reprend le projet (Claude, Codex, Cursor, Copilot, Gemini, etc.). Il donne les règles à respecter, la méthode de travail et le journal des changements.

**Le dépôt est public.** N'y écris jamais de prix de prestation, de données personnelles ni de documents du client.

## À lire avant de toucher au projet

1. [`README.md`](README.md) : les décisions, le plan des pages, les données manquantes et les **prochaines étapes**, qui servent de liste de tâches.
2. [`DESIGN.md`](DESIGN.md) : le design system. Lis-le avant de toucher à une page, et garde-le aligné avec `style.css`.
3. Le journal ci-dessous : ce qui a été fait et quand.

## Le projet en bref

- C'est le site vitrine du restaurant **Chef Eyad Tunisia** (Berges du Lac 2, Tunis), exploité par la SARL Panorient.
- Il est statique et en trois langues : français (défaut), arabe (RTL) et anglais.
- Les textes sont dans `i18n.json`, les gabarits dans `templates/` et le style dans `style.css`. `python3 build.py` génère `docs/{fr,ar,en}/`.
- Préproduction : GitHub Pages (`main`, `/docs`), redéployé à chaque push. Production prévue : un VPS OVH, pas encore déployé.
- Aperçu local : `cd docs && python3 -m http.server 8000`.

## Règles impératives

- **On avance pas à pas avec le propriétaire du projet.** Il valide chaque étape : ne code rien qu'il n'a pas demandé.
- **Ne publie aucune information sans source ni validation du client** : prix, horaires, chiffres. Ce qui manque s'affiche « à venir » ou « à confirmer ».
- **Ne modifie jamais `docs/` à la main** : le dossier est écrasé à chaque génération.
- **Ne versionne pas** `photos-client/` (à part ses index CSV) ni `documents-client/`.
- Contenu :
  - ne cite jamais Kafr Qasim ;
  - en arabe, écris « خروف » et jamais « ضأن » ;
  - dans les chaînes arabes, écris `Chef&nbsp;Eyad` ;
  - la maison propose **3 sauces maison**, jamais « 15 sauces » ;
  - le fumage dure **10 à 12 h** ;
  - n'aligne pas le français ni l'anglais sur l'arabe sans demande.
- Photos : uniquement celles de `photos-client/`, en suivant les règles de la section « Photos » du README. Pas d'image IA ni de photo prise sur internet.
- N'ajoute aucun cookie ni aucun appel à un tiers au chargement de la page, car la page Confidentialité s'engage à ne pas en avoir.

## Après chaque modification (obligatoire)

1. Régénère le site avec `python3 build.py` et vérifie le résultat dans les trois langues.
2. **Mets à jour `README.md`** : les décisions, les données manquantes et les prochaines étapes (coche ou ajoute les points concernés).
3. **Ajoute une ligne au journal ci-dessous** : la date, ce qui a été fait et le commit.
4. Commite avec un message clair en français (`feat:`, `fix:`, `docs:`).

## Journal

| Date | Fait | Commit |
|---|---|---|
| 02/10/2026 | Les 6 pages sont designées et GitHub Pages est activé. Photothèque du client rapatriée ; les images IA et la photo internet sont archivées | bc1d69c |
| 07/10/2026 | Textes arabes du client, page Confidentialité et mentions légales (Panorient, sans cookie), boissons, salon VIP, réseau international dans À propos, horaires de la carte | e09e15b → 76c5119 |
| 10/10/2026 | README mis à jour (statut, hébergement VPS OVH, prochaines étapes) et création de ce fichier de suivi | voir `git log` |
| 10/10/2026 | Le client a validé les textes et les photos, et l'accès au VPS est obtenu (README mis à jour) | voir `git log` |
