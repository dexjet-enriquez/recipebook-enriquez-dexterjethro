# Recipebook

A small Django web app for keeping recipes and the ingredients they call for. Recipes are managed through the Django admin and browsed through a public list and detail view.

## Requirements

- Python 3.10+
- Django 6.0

## Setup

```bash
# from the repository root
python3 -m venv myenv
source myenv/bin/activate        # Windows: myenv\Scripts\activate
pip install django

cd recipebook
python manage.py migrate
python manage.py createsuperuser   # required — see below
python manage.py runserver
```

The app runs at http://127.0.0.1:8000/.

### Creating the admin account

`createsuperuser` is not optional here. The admin at `/admin/` is the only place
recipes can be added — there are no create or edit views on the public side — so
without an account you get a running server, an empty database, and no way to put
anything in it.

The command prompts for a username, an email (which can be left blank), and a
password. Then log in at http://127.0.0.1:8000/admin/ and add a recipe; the form
has an inline editor for its ingredients and quantities. Once a recipe exists it
shows up at `/recipes/list`.

If you forget the password later, reset it with:

```bash
python manage.py changepassword <username>
```

## URLs

| Path | View | Description |
| --- | --- | --- |
| `/recipes/list` | `RecipeListView` | All recipes, alphabetical |
| `/recipe/<pk>` | `RecipeDetailView` | One recipe with its ingredients and quantities |
| `/admin/` | Django admin | Add and edit recipes |

Recipes are created in the admin at `/admin/`. The recipe form includes an inline
editor for its ingredients, so a recipe and its quantities are entered on one page.

## Models

Defined in [models.py](recipebook/ledger/models.py):

- **`Ingredient`** — a name, e.g. "flour". Reusable across recipes.
- **`Recipe`** — a name, e.g. "pancakes".
- **`RecipeIngredient`** — the join between the two, plus a free-text `quantity`
  (e.g. "2 cups"). Deleting a recipe or an ingredient cascades to its rows here.

A recipe reaches its ingredient rows through `recipe.ingredients.all`, which the
detail template uses to render the list.

## Project layout

```
recipebook/
├── manage.py
├── recipebook/            # project settings, root URLconf, WSGI/ASGI
│   ├── settings.py
│   └── urls.py
├── ledger/                # the app
│   ├── models.py          # Ingredient, Recipe, RecipeIngredient
│   ├── views.py           # RecipeListView, RecipeDetailView
│   ├── urls.py            # namespaced under "ledger"
│   ├── admin.py           # Recipe admin with inline ingredients
│   ├── migrations/
│   └── templates/ledger/  # recipe_list.html, recipe_detail.html
└── templates/
    └── base.html          # shared layout
```

## Notes

- The database is SQLite (`recipebook/db.sqlite3`), which is gitignored — run
  `migrate` after cloning to create it.
- `DEBUG = True` and the default `SECRET_KEY` are still in
  [settings.py](recipebook/recipebook/settings.py). Both need to change before
  this is deployed anywhere public.
