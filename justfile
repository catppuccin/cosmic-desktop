_default:
  @just --list

clean:
  rm -r themes | true

build: clean
  whiskers templates/cosmic-settings.tera
  whiskers templates/cosmic-term.tera
