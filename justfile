_default:
  @just --list

clean:
  rm -r cosmic-settings cosmic-term | true

build: clean
  whiskers templates/cosmic-settings.tera
  mv themes cosmic-settings
  whiskers templates/cosmic-term.tera
  mv themes cosmic-term
