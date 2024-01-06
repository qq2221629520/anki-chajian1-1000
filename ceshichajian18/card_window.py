from .anki_version_detection import anki_point_version
from .config import gc

from anki.cards import Card

import aqt
from aqt.previewer import Previewer
from aqt.qt import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QKeySequence,
    QPushButton,
    qconnect,
)
from aqt.utils import tooltip

from .link_handler import process_urlcmd
from .note_edit import external_note_dialog




if anki_point_version <= 28:
    from aqt.previewer import SingleCardPreviewer
else:
    # commit 61e8611b from 2020-07-24 removed the class SingleCardPreviewer
    # with the comment "fix lint issue in previewer, and drop unused code"
    # see  https://github.com/ankitects/anki/commit/61e8611b7baa292c43693669fc79b7ae552e8585#diff-14b1ab9e8b1d0712f88edd6e359790a8
    class SingleCardPreviewer(Previewer):
        def __init__(self, card: Card, *args, **kwargs):
            self._card = card
            super().__init__(*args, **kwargs)

        def card(self) -> Card:
            return self._card

        def _create_gui(self):
            super()._create_gui()
            self._other_side = self.bbox.addButton(
                "Other side", QDialogButtonBox.ButtonRole.ActionRole
            )
            self._other_side.setAutoDefault(False)
            self._other_side.setShortcut(QKeySequence("Right"))
            self._other_side.setShortcut(QKeySequence("Left"))
            self._other_side.setToolTip("Shortcut key: Left or Right arrow")
            qconnect(self._other_side.clicked, self._on_other_side)

        def _on_other_side(self):
            if self._state == "question":
                self._state = "answer"
            else:
                self._state = "question"
            self.render_card()

        def card_changed(self):
           return True


class SingleCardPreviewerMod(SingleCardPreviewer):
    def _on_bridge_cmd(self, cmd):
        super()._on_bridge_cmd(cmd)

    def _create_gui(self):
        super()._create_gui()

        self.vbox.removeWidget(self.bbox)
        self.bottombar = QHBoxLayout()

        self.browser_button = QPushButton("show in browser")
        #self.browser_button.setShortcut(QKeySequence("b"))
        #self.browser_button.setToolTip("Shortcut key: %s" % "b")
        self.browser_button.clicked.connect(self._on_browser_button)
        self.bottombar.addWidget(self.browser_button)

        self.edit_button = self.bbox.addButton("edit", QDialogButtonBox.ButtonRole.HelpRole)
        #self.edit_button.setShortcut(QKeySequence("e"))
        #self.edit_button.setToolTip("Shortcut key: %s" % "e")
        self.edit_button.clicked.connect(self._on_edit_button)
        self.bottombar.addWidget(self.edit_button)

        self.showRate = QPushButton("G")  # grade - "R" is already used for replay audio
        self.showRate.setFixedWidth(25)
        # self.showRate.setShortcut(QKeySequence("g"))
        # self.showRate.setToolTip("Shortcut key: %s" % "G")
        self.showRate.clicked.connect(self.onShowRatingBar)
        # self.bottombar.addWidget(self.showRate)

        self.bottombar.addWidget(self.bbox)
        self.vbox.addLayout(self.bottombar)

    def _setup_web_view(self):
        super()._setup_web_view()
        for child in self.bbox.children():
            if isinstance(child, QCheckBox):
                self.both_sides_button = child
        self._show_both_sides = self.check_preview_both_config()
        self.both_sides_button.setChecked(self._show_both_sides)

    def check_preview_both_config(self):
        # if True both sides are shown
        showboth = False
        if gc("card_preview__default_is_answer"):
            showboth ^= True
        overrides = gc("card_preview__override_toggle_from_default_for_notetypes")
        if anki_point_version <= 49:
            name = self.card().model()['name']
        else:
            name = self.card().note_type()['name']
        if name in overrides:
            showboth ^= True
        return showboth

    def _on_browser_button(self):
        tooltip('browser clicked')
        browser = aqt.dialogs.open("Browser", self.mw)
        query = '"nid:' + str(self.card().nid) + '"'
        browser.form.searchEdit.lineEdit().setText(query)
        browser.onSearchActivated()

    def _on_edit_button(self):
        note = self.mw.col.getNote(self.card().nid)
        external_note_dialog(note)
        QDialog.reject(self)

    def onShowRatingBar(self):
        pass


def external_card_dialog(card):
    d = SingleCardPreviewerMod(card=card, parent=aqt.mw, mw=aqt.mw, on_close=lambda:None)
    d.open()
