_default:
  @just --list

clean:
  rm -rf themes

build: clean
  whiskers templates/cosmic-settings.tera
  whiskers templates/cosmic-term.tera
