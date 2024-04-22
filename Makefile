GEN=generate.py
TERM=cosmic-term.py
THEME_DIR=cosmic-settings
TERM_DIR=cosmic-term
MOCHA=$(THEME_DIR)/Catppuccin-Mocha-Lavender.ron
FRAPPE=$(THEME_DIR)/Catppuccin-frappe-Lavender.ron
MACCHIATO=$(THEME_DIR)/Catppuccin-Macchiato-Lavender.ron
LATTE=$(THEME_DIR)/Catppuccin-Latte-Lavender.ron

all: theme termscheme

theme: $(MOCHA) $(FRAPPE) $(MACCHIATO) $(LATTE)

$(MOCHA): $(GEN)
	python $< mocha > $@

$(FRAPPE): $(GEN)
	python $< frappe > $@

$(MACCHIATO): $(GEN)
	python $< macchiato > $@

$(LATTE): $(GEN)
	python $< latte > $@

termscheme: $(TERM)
	python $<

clean:
	rm -f $(MOCHA) $(FRAPPE) $(MACCHIATO) $(LATTE) $(TERM_DIR)/*.ron
