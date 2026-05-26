from __future__ import annotations

FONT_FAMILY = "Segoe UI"
FONT_POINT_SIZE = 10

SPACE_0 = 0
SPACE_1 = 4
SPACE_2 = 8
SPACE_3 = 12
SPACE_4 = 16
SPACE_5 = 20
SPACE_6 = 24
SPACE_7 = 28
SPACE_8 = 32
SPACE_12 = 48
HAIRLINE = 1

TEXT_XS = "11px"
TEXT_SM = "13px"
TEXT_BASE = "15px"
TEXT_LG = "17px"
TEXT_XL = "20px"
TEXT_2XL = "24px"
TEXT_PAGER = "28px"

LINE_XS = "16px"
LINE_SM = "18px"
LINE_BASE = "20px"
LINE_LG = "24px"
LINE_XL = "28px"
LINE_2XL = "32px"

RADIUS_SM = "4px"
RADIUS_MD = "6px"
RADIUS_LG = "8px"

DURATION_FAST_MS = 120
DURATION_BASE_MS = 200
EASING_STANDARD = "cubic-bezier(0.4, 0, 0.2, 1)"

COLOR_BG = "#0B0F14"
COLOR_BG_SIDEBAR = "#090D12"
COLOR_SURFACE = "#121923"
COLOR_SURFACE_ALT = "#0F1724"
COLOR_SURFACE_MUTED = "#141A22"
COLOR_SURFACE_HOVER = "#1A2530"
COLOR_SURFACE_ACTIVE = "#101820"
COLOR_BORDER = "#263241"
COLOR_BORDER_MUTED = "#1F2935"
COLOR_BORDER_STRONG = "#3F6E8D"

COLOR_TEXT_PRIMARY = "#F4F7FB"
COLOR_TEXT_SECONDARY = "#D3DCE7"
COLOR_TEXT_MUTED = "#9EADBD"
COLOR_TEXT_DISABLED = "#6F7E8E"
COLOR_TEXT_INVERSE = COLOR_TEXT_PRIMARY

COLOR_PRIMARY = "#2F7DB8"
COLOR_PRIMARY_HOVER = "#3C92D0"
COLOR_PRIMARY_ACTIVE = "#23618F"
COLOR_PRIMARY_MUTED = "#14283A"
COLOR_PRIMARY_SOFT = "#7DB7E0"
COLOR_PRIMARY_BORDER = "#4F97C5"
COLOR_FOCUS = "#86C5EA"
COLOR_SELECTION = "#1F5E86"

COLOR_SUCCESS = "#4CC38A"
COLOR_SUCCESS_BG = "#102C23"
COLOR_SUCCESS_BORDER = "#2D7657"
COLOR_WARNING = "#E6B84A"
COLOR_WARNING_BG = "#342814"
COLOR_WARNING_BORDER = "#7A6126"
COLOR_DANGER = "#F06B6B"
COLOR_DANGER_BG = "#351A1E"
COLOR_DANGER_BORDER = "#824147"
COLOR_INFO = "#7DB7E0"
COLOR_INFO_BG = "#132738"
COLOR_INFO_BORDER = "#345B78"

CONTROL_HEIGHT = 34
CONTROL_HEIGHT_COMPACT = 30
CHIP_HEIGHT = 24
PAGER_SIZE = 30
TABLE_ROW_HEIGHT = 34
SERVERS_TABLE_ROW_HEIGHT = 42
SERVER_TABLE_CHECK_COLUMN_WIDTH = 48
SERVER_TABLE_PROTOCOL_COLUMN_WIDTH = 120
SERVER_TABLE_PROTOCOL_BADGE_MIN_WIDTH = 88
SERVER_TABLE_PROTOCOL_BADGE_HEIGHT = 24
ICON_SIZE_SM = 16
HERO_METRIC_ICON_SIZE = 18
ICON_SIZE_MD = 20
ICON_SIZE_LG = 24
ICON_SIZE_XL = 36
BUTTON_MIN_WIDTH = 96
SERVER_SELECTION_CARD_HEIGHT = 60
CONNECTION_SERVER_LIST_VISIBLE_ROWS = 4
CONNECTION_SERVER_LIST_HEIGHT = (
    SERVER_SELECTION_CARD_HEIGHT * CONNECTION_SERVER_LIST_VISIBLE_ROWS
    + SPACE_1 * (CONNECTION_SERVER_LIST_VISIBLE_ROWS - 1)
)

SHADOW_SM = "none"
SHADOW_MD = "none"


def px(value: int | float) -> str:
    return f"{value:g}px"


def spacing(*values: int) -> tuple[int, ...]:
    return values


def app_stylesheet() -> str:
    values = {
        "font_family": FONT_FAMILY,
        "text_xs": TEXT_XS,
        "text_sm": TEXT_SM,
        "text_base": TEXT_BASE,
        "text_lg": TEXT_LG,
        "text_xl": TEXT_XL,
        "text_2xl": TEXT_2XL,
        "text_pager": TEXT_PAGER,
        "line_xs": LINE_XS,
        "line_sm": LINE_SM,
        "line_base": LINE_BASE,
        "line_lg": LINE_LG,
        "line_xl": LINE_XL,
        "line_2xl": LINE_2XL,
        "radius_sm": RADIUS_SM,
        "radius_md": RADIUS_MD,
        "radius_lg": RADIUS_LG,
        "bg": COLOR_BG,
        "bg_sidebar": COLOR_BG_SIDEBAR,
        "surface": COLOR_SURFACE,
        "surface_alt": COLOR_SURFACE_ALT,
        "surface_muted": COLOR_SURFACE_MUTED,
        "surface_hover": COLOR_SURFACE_HOVER,
        "surface_active": COLOR_SURFACE_ACTIVE,
        "border": COLOR_BORDER,
        "border_muted": COLOR_BORDER_MUTED,
        "border_strong": COLOR_BORDER_STRONG,
        "text_primary": COLOR_TEXT_PRIMARY,
        "text_secondary": COLOR_TEXT_SECONDARY,
        "text_muted": COLOR_TEXT_MUTED,
        "text_disabled": COLOR_TEXT_DISABLED,
        "text_inverse": COLOR_TEXT_INVERSE,
        "primary": COLOR_PRIMARY,
        "primary_hover": COLOR_PRIMARY_HOVER,
        "primary_active": COLOR_PRIMARY_ACTIVE,
        "primary_muted": COLOR_PRIMARY_MUTED,
        "primary_soft": COLOR_PRIMARY_SOFT,
        "primary_border": COLOR_PRIMARY_BORDER,
        "focus": COLOR_FOCUS,
        "selection": COLOR_SELECTION,
        "success": COLOR_SUCCESS,
        "success_bg": COLOR_SUCCESS_BG,
        "success_border": COLOR_SUCCESS_BORDER,
        "warning": COLOR_WARNING,
        "warning_bg": COLOR_WARNING_BG,
        "warning_border": COLOR_WARNING_BORDER,
        "danger": COLOR_DANGER,
        "danger_bg": COLOR_DANGER_BG,
        "danger_border": COLOR_DANGER_BORDER,
        "info": COLOR_INFO,
        "info_bg": COLOR_INFO_BG,
        "info_border": COLOR_INFO_BORDER,
        "space_0": px(SPACE_0),
        "space_1": px(SPACE_1),
        "space_2": px(SPACE_2),
        "space_3": px(SPACE_3),
        "space_4": px(SPACE_4),
        "space_5": px(SPACE_5),
        "space_6": px(SPACE_6),
        "space_7": px(SPACE_7),
        "space_8": px(SPACE_8),
        "space_12": px(SPACE_12),
        "control_height": px(CONTROL_HEIGHT),
        "control_compact_height": px(CONTROL_HEIGHT_COMPACT),
        "chip_height": px(CHIP_HEIGHT),
        "pager_size": px(PAGER_SIZE),
        "table_row_height": px(TABLE_ROW_HEIGHT),
        "icon_size_sm": px(ICON_SIZE_SM),
        "hero_metric_icon_size": px(HERO_METRIC_ICON_SIZE),
        "icon_size_md": px(ICON_SIZE_MD),
        "button_min_width": px(BUTTON_MIN_WIDTH),
    }
    return _APP_STYLESHEET % values


_APP_STYLESHEET = """
* {
    font-family: "%(font_family)s";
    font-size: %(text_sm)s;
}
QMainWindow, QWidget, QDialog {
    background: %(bg)s;
    color: %(text_primary)s;
    selection-background-color: %(selection)s;
    selection-color: %(text_inverse)s;
}
QLabel, QCheckBox {
    background: transparent;
    border: 0;
}
QWidget#Content,
QWidget#ServersPage {
    background: %(bg)s;
    color: %(text_primary)s;
}
QWidget#Transparent,
QFrame#Toolbar,
QFrame#ServersSearchBar,
QFrame#ServersImportBar,
QFrame#ServersActionBar,
QFrame#ServersFooter {
    background: transparent;
    border: 0;
    padding: %(space_0)s;
}
QFrame#Sidebar {
    background: %(bg_sidebar)s;
    border-right: 1px solid %(border)s;
}
QFrame#SidebarOperationPanel {
    background: %(surface_alt)s;
    border: 1px solid %(border_muted)s;
    border-radius: %(radius_md)s;
}
QFrame#Panel,
QFrame#TableSurface,
QFrame#ServersSearchCard,
QFrame#EmptyState,
QFrame#ServerDetailsPanel,
QFrame#ServerSelectionCard {
    background: %(surface)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_md)s;
}
QFrame#TableSurface {
    background: %(surface_alt)s;
    border-color: %(border_muted)s;
}
QFrame#ConnectionHero {
    background: %(surface)s;
    border: 1px solid %(border_strong)s;
    border-radius: %(radius_md)s;
}
QFrame#ConnectionRouteCard {
    background: %(surface_alt)s;
    border: 1px solid %(border_muted)s;
    border-radius: %(radius_md)s;
}
QWidget#ConnectionRouteMetric {
    background: %(surface)s;
    border: 1px solid %(border_muted)s;
    border-radius: %(radius_sm)s;
    min-height: %(control_height)s;
}
QScrollArea#ConnectionServerScroll,
QWidget#ConnectionServerViewport,
QWidget#ConnectionServerList {
    background: %(surface)s;
    border: 0;
}
QFrame#ServerSelectionCard:hover {
    background: %(surface_hover)s;
    border-color: %(primary_border)s;
}
QFrame#ServerSelectionCard[state="selected"] {
    background: %(primary_muted)s;
    border-color: %(primary_border)s;
}
QFrame#ServerSelectionCard:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
}
QScrollArea#ServerDetailsScroll,
QWidget#ServerDetailsViewport,
QWidget#ServerDetailsBody {
    background: transparent;
    border: 0;
}
QWidget#ServerDetailCell {
    background: %(surface_alt)s;
    border: 1px solid %(border_muted)s;
    border-radius: %(radius_md)s;
}
QWidget#ServerDetailCell:hover {
    background: %(surface_hover)s;
    border-color: %(border_strong)s;
}
QLabel#AppTitle {
    background: transparent;
    color: %(text_primary)s;
    font-size: %(text_xl)s;
    font-weight: 700;
    line-height: %(line_xl)s;
}
QLabel#SidebarOperationTitle {
    background: transparent;
    color: %(primary_soft)s;
    font-size: %(text_xs)s;
    font-weight: 800;
    line-height: %(line_xs)s;
}
QLabel#SidebarOperationMessage {
    background: transparent;
    color: %(text_secondary)s;
    font-size: %(text_xs)s;
    line-height: %(line_xs)s;
}
QProgressBar#SidebarOperationProgress {
    background: %(surface_muted)s;
    border: 0;
    border-radius: 2px;
    max-height: %(space_1)s;
    min-height: %(space_1)s;
}
QProgressBar#SidebarOperationProgress::chunk {
    background: %(primary)s;
    border-radius: 2px;
}
QLabel#ConnectionServerCount {
    background: transparent;
    color: %(text_secondary)s;
    font-size: %(text_xs)s;
    line-height: %(line_xs)s;
}
QListWidget#Navigation {
    background: transparent;
    border: 0;
    outline: 0;
    color: %(text_secondary)s;
}
QListWidget#Navigation::item {
    border-radius: %(radius_md)s;
    min-height: %(space_7)s;
    padding: %(space_1)s %(space_3)s;
}
QListWidget#Navigation::item:selected {
    background: %(selection)s;
    color: %(text_inverse)s;
}
QListWidget#Navigation::item:hover {
    background: %(surface_hover)s;
    color: %(text_primary)s;
}
QLabel#PageTitle {
    background: transparent;
    color: %(text_primary)s;
    font-size: %(text_2xl)s;
    font-weight: 700;
    line-height: %(line_2xl)s;
}
QLabel#PageSubtitle,
QLabel#ConnectionStatusDetail,
QLabel#ConnectionServerMeta,
QLabel#EmptyText {
    background: transparent;
    color: %(text_secondary)s;
    font-size: %(text_sm)s;
    line-height: %(line_sm)s;
}
QLabel#BestServerCaption,
QLabel#FieldCaption,
QLabel#PanelTitle,
QLabel#HeroMetricCaption,
QLabel#ConnectionRouteCaption {
    background: transparent;
    color: %(text_muted)s;
    font-size: %(text_xs)s;
    font-weight: 600;
    line-height: %(line_xs)s;
}
QLabel#BestServerName,
QLabel#FieldValue,
QLabel#EmptyTitle,
QLabel#ConnectionServerTitle,
QLabel#HeroMetricValue,
QLabel#ConnectionRouteValue {
    background: transparent;
    color: %(text_primary)s;
    font-size: %(text_sm)s;
    font-weight: 700;
    line-height: %(line_sm)s;
}
QLabel#ConnectionStatusBadge {
    background: transparent;
    color: %(text_primary)s;
    font-size: %(text_xl)s;
    font-weight: 800;
    line-height: %(line_xl)s;
    min-height: %(space_7)s;
    padding: %(space_0)s;
}
QLabel#ConnectionServerTitle {
    font-size: %(text_lg)s;
    font-weight: 800;
    line-height: %(line_lg)s;
    min-height: %(space_6)s;
}
QLabel#ConnectionStatusBadge[state="connected"] {
    color: %(success)s;
}
QLabel#ConnectionStatusBadge[state="busy"] {
    color: %(info)s;
}
QLabel#ConnectionStatusBadge[state="error"] {
    color: %(danger)s;
}
QLabel#ConnectionStatusBadge[state="disconnected"] {
    color: %(warning)s;
}
QFrame#HeroSeparator,
QFrame#HeroMetricDivider {
    background: %(border_muted)s;
    border: 0;
}
QWidget#HeroMetric {
    background: transparent;
    border: 0;
    min-height: %(control_height)s;
}
QLabel#HeroMetricIcon {
    background: transparent;
    border: 0;
    color: %(primary_soft)s;
    font-size: %(text_2xl)s;
    font-weight: 800;
    min-height: %(hero_metric_icon_size)s;
    min-width: %(hero_metric_icon_size)s;
    max-height: %(hero_metric_icon_size)s;
    max-width: %(hero_metric_icon_size)s;
}
QLabel#ServerCardIcon {
    background: %(primary_muted)s;
    border: 1px solid %(primary_border)s;
    border-radius: %(radius_md)s;
    color: %(primary_soft)s;
    font-size: %(text_base)s;
    font-weight: 800;
}
QLabel#ServerCardTitle {
    background: transparent;
    color: %(text_primary)s;
    font-size: %(text_sm)s;
    font-weight: 700;
}
QLabel#ServerCardMeta {
    background: transparent;
    color: %(text_secondary)s;
    font-size: %(text_xs)s;
}
QLabel#BestPingBadge,
QLabel#ServerCardPing,
QLabel#ServerCardSelected,
QLabel#ProtocolBadge,
QLabel#SourceBadge,
QLabel#PingBadge,
QLabel#StatusPill {
    background: %(surface_alt)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_sm)s;
    color: %(text_secondary)s;
    font-size: %(text_xs)s;
    font-weight: 800;
    min-height: %(chip_height)s;
    padding: %(space_1)s %(space_2)s;
}
QLabel#ProtocolBadge {
    min-height: %(space_5)s;
    padding: 1px %(space_2)s;
}
QLabel#ProtocolBadge[state="vless"],
QLabel#ProtocolBadge[state="vmess"],
QLabel#ProtocolBadge[state="trojan"],
QLabel#ProtocolBadge[state="amneziawg"],
QLabel#ProtocolBadge[state="other"] {
    background: %(primary_muted)s;
    border-color: %(border_strong)s;
    color: %(primary_soft)s;
}
QLabel#SourceBadge[state="manual"],
QLabel#BestPingBadge[state="unknown"],
QLabel#PingBadge[state="unknown"],
QLabel#StatusPill[state="unknown"] {
    background: %(surface_alt)s;
    border-color: %(border)s;
    color: %(text_secondary)s;
}
QLabel#SourceBadge[state="subscription"] {
    background: %(info_bg)s;
    border-color: %(info_border)s;
    color: %(info)s;
}
QLabel#BestPingBadge,
QLabel#BestPingBadge[state="ok"],
QLabel#ServerCardPing[state="ok"],
QLabel#PingBadge[state="ok"],
QLabel#StatusPill[state="ok"],
QLabel#StatusPill[state="active"] {
    background: %(success_bg)s;
    border-color: %(success_border)s;
    color: %(success)s;
}
QLabel#BestPingBadge[state="slow"],
QLabel#PingBadge[state="slow"],
QLabel#StatusPill[state="slow"] {
    background: %(warning_bg)s;
    border-color: %(warning_border)s;
    color: %(warning)s;
}
QLabel#BestPingBadge[state="udp"],
QLabel#PingBadge[state="udp"],
QLabel#StatusPill[state="udp"] {
    background: %(info_bg)s;
    border-color: %(info_border)s;
    color: %(info)s;
}
QLabel#BestPingBadge[state="error"],
QLabel#PingBadge[state="error"],
QLabel#StatusPill[state="error"] {
    background: %(danger_bg)s;
    border-color: %(danger_border)s;
    color: %(danger)s;
}
QLabel#ServerCardSelected {
    background: %(primary)s;
    border-color: %(primary_border)s;
    color: %(text_inverse)s;
}
QFrame#ConnectionServerEmpty {
    background: %(surface)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_md)s;
}
QLabel#ConnectionServerEmptyTitle {
    background: transparent;
    border: 0;
    color: %(text_primary)s;
    font-size: %(text_base)s;
    font-weight: 800;
}
QLabel#ConnectionServerEmptyText {
    background: transparent;
    border: 0;
    color: %(text_muted)s;
    font-size: %(text_sm)s;
}
QGroupBox {
    background: transparent;
    border: 0;
    margin-top: %(space_0)s;
    padding: %(space_0)s;
    font-weight: 600;
}
QGroupBox::title {
    color: transparent;
    background: transparent;
    border: 0;
    padding: %(space_0)s;
    height: %(space_0)s;
    margin: %(space_0)s;
}
QFrame#Panel > QLabel {
    background: transparent;
    border: 0;
}
QPushButton {
    background: %(surface)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_md)s;
    color: %(text_primary)s;
    font-weight: 600;
    min-height: %(control_height)s;
    padding: %(space_1)s %(space_3)s;
}
QPushButton:hover {
    background: %(surface_hover)s;
    border-color: %(primary_border)s;
    color: %(text_inverse)s;
}
QPushButton:pressed {
    background: %(surface_active)s;
    border-color: %(primary_soft)s;
}
QPushButton:focus {
    border-color: %(focus)s;
}
QPushButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton[alignedIconButton="true"] {
    text-align: left;
    padding-left: %(space_3)s;
    padding-right: %(space_3)s;
}
QPushButton#PrimaryButton {
    background: %(primary)s;
    border-color: %(primary_border)s;
    color: %(text_inverse)s;
}
QPushButton#ConnectionCompactPrimaryButton {
    background: %(primary)s;
    border: 1px solid %(primary_border)s;
    border-radius: %(radius_md)s;
    color: %(text_inverse)s;
    font-size: %(text_xs)s;
    font-weight: 700;
    min-height: %(control_height)s;
    padding: %(space_1)s %(space_2)s;
}
QPushButton#ConnectionPrimaryButton {
    background: %(primary)s;
    border: 1px solid %(primary_border)s;
    border-radius: %(radius_lg)s;
    color: %(text_inverse)s;
    font-size: %(text_lg)s;
    font-weight: 800;
    min-height: %(space_7)s;
    padding: %(space_3)s %(space_6)s;
}
QPushButton#PrimaryButton:hover {
    background: %(primary_hover)s;
    border-color: %(primary_soft)s;
}
QPushButton#ConnectionCompactPrimaryButton:hover {
    background: %(primary_hover)s;
    border-color: %(primary_soft)s;
}
QPushButton#ConnectionPrimaryButton:hover {
    background: %(primary_hover)s;
    border-color: %(focus)s;
}
QPushButton#PrimaryButton:pressed {
    background: %(primary_active)s;
}
QPushButton#ConnectionCompactPrimaryButton:pressed {
    background: %(primary_active)s;
}
QPushButton#ConnectionPrimaryButton:pressed {
    background: %(primary_active)s;
}
QPushButton#PrimaryButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton#ConnectionCompactPrimaryButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton#ConnectionPrimaryButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton#DangerButton {
    background: %(danger_bg)s;
    border-color: %(danger_border)s;
    color: %(danger)s;
}
QPushButton#DangerButton:hover {
    background: %(danger_border)s;
    border-color: %(danger)s;
    color: %(text_inverse)s;
}
QPushButton#DangerButton:pressed {
    background: %(danger_bg)s;
}
QPushButton#DangerButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton#FavoriteButton {
    background: %(surface)s;
    border-color: %(border)s;
    color: %(text_secondary)s;
}
QPushButton#FavoriteButton[state="active"] {
    background: %(warning_bg)s;
    border-color: %(warning_border)s;
    color: %(warning)s;
}
QPushButton#FavoriteButton:hover,
QPushButton#FavoriteButton[state="active"]:hover {
    background: %(surface_hover)s;
    border-color: %(primary)s;
    color: %(text_inverse)s;
}
QPushButton#FavoriteButton:pressed {
    background: %(surface_active)s;
}
QPushButton#FavoriteButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton#SubtleButton {
    background: %(surface_alt)s;
    border-color: %(border)s;
    color: %(text_secondary)s;
}
QPushButton#SubtleButton:hover {
    background: %(surface_hover)s;
    border-color: %(primary)s;
}
QPushButton#SubtleButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton#OutlinedButton {
    background: transparent;
    border-color: %(primary_border)s;
    color: %(primary_soft)s;
}
QPushButton#ConnectionCompactOutlinedButton {
    background: transparent;
    border: 1px solid %(primary_border)s;
    border-radius: %(radius_md)s;
    color: %(primary_soft)s;
    font-size: %(text_xs)s;
    font-weight: 700;
    min-height: %(control_height)s;
    padding: %(space_1)s %(space_2)s;
}
QPushButton#OutlinedButton:hover {
    background: %(primary_muted)s;
    border-color: %(primary_soft)s;
    color: %(text_inverse)s;
}
QPushButton#ConnectionCompactOutlinedButton:hover {
    background: %(primary_muted)s;
    border-color: %(primary_soft)s;
    color: %(text_inverse)s;
}
QPushButton#OutlinedButton:pressed {
    background: %(surface_active)s;
    border-color: %(primary)s;
}
QPushButton#ConnectionCompactOutlinedButton:pressed {
    background: %(surface_active)s;
    border-color: %(primary)s;
}
QPushButton#OutlinedButton:disabled {
    background: transparent;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QPushButton#ConnectionCompactOutlinedButton:disabled {
    background: transparent;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QLineEdit, QTextEdit, QComboBox {
    background: %(surface_alt)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_md)s;
    color: %(text_primary)s;
    min-height: %(control_height)s;
    padding: %(space_1)s %(space_3)s;
}
QLineEdit:hover, QTextEdit:hover, QComboBox:hover {
    border-color: %(border_strong)s;
}
QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
    border-color: %(focus)s;
    background: %(surface)s;
}
QLineEdit:disabled, QTextEdit:disabled, QComboBox:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QComboBox::drop-down {
    border: 0;
    width: %(space_8)s;
}
QComboBox QAbstractItemView {
    background: %(surface)s;
    border: 1px solid %(border)s;
    color: %(text_primary)s;
    selection-background-color: %(selection)s;
    selection-color: %(text_inverse)s;
    outline: 0;
}
QCheckBox {
    color: %(text_secondary)s;
    spacing: %(space_2)s;
}
QCheckBox:hover {
    color: %(text_primary)s;
}
QCheckBox:disabled {
    color: %(text_disabled)s;
}
QCheckBox::indicator {
    background: %(surface_alt)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_sm)s;
    height: %(icon_size_sm)s;
    width: %(icon_size_sm)s;
}
QCheckBox::indicator:hover,
QCheckBox::indicator:focus {
    border-color: %(focus)s;
}
QCheckBox::indicator:checked {
    background: %(primary)s;
    border-color: %(primary_soft)s;
}
QCheckBox::indicator:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
}
QTableWidget, QTableView {
    background: transparent;
    alternate-background-color: %(surface)s;
    border: 0;
    border-radius: 0;
    color: %(text_primary)s;
    gridline-color: transparent;
    outline: 0;
}
QTableWidget::viewport, QTableView::viewport {
    background: %(surface_alt)s;
    border: 0;
    border-radius: 0;
}
QTableWidget::item, QTableView::item {
    border: 0;
    padding: %(space_1)s %(space_3)s;
}
QTableWidget::item:hover, QTableView::item:hover {
    background: %(surface_hover)s;
}
QTableWidget::item:selected, QTableView::item:selected,
QTableWidget#ServersTable::item:selected {
    background: %(selection)s;
    border: 0;
    color: %(text_inverse)s;
}
QHeaderView::section {
    background: %(surface_alt)s;
    border: 0;
    border-bottom: 1px solid %(border)s;
    color: %(text_muted)s;
    font-weight: 700;
    padding: %(space_2)s %(space_3)s;
}
QTableWidget#ServersTable::item {
    border-bottom: 1px solid %(border_muted)s;
    padding: %(space_1)s %(space_2)s;
}
QTableWidget#ServersTable::item:hover {
    background: %(surface_hover)s;
}
QTableWidget#ServersTable::item:selected {
    background: %(selection)s;
    color: %(text_inverse)s;
}
QTableWidget#ServersTable::indicator {
    width: %(icon_size_sm)s;
    height: %(icon_size_sm)s;
    border-radius: %(radius_sm)s;
    border: 1px solid %(text_disabled)s;
    background: %(bg)s;
    margin: %(space_1)s;
}
QTableWidget#ServersTable::indicator:checked {
    background: %(primary)s;
    border: 1px solid %(primary_soft)s;
    image: none;
}
QLabel#PagerCurrent {
    background: %(selection)s;
    border: 1px solid %(primary_border)s;
    border-radius: %(radius_md)s;
    color: %(text_inverse)s;
    font-weight: 800;
    min-height: %(pager_size)s;
    min-width: %(pager_size)s;
    max-height: %(pager_size)s;
    max-width: %(pager_size)s;
}
QPushButton#PagerButton {
    background: %(surface_alt)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_md)s;
    color: %(text_muted)s;
    font-size: %(text_pager)s;
    font-weight: 800;
    min-height: %(pager_size)s;
    min-width: %(pager_size)s;
    max-height: %(pager_size)s;
    max-width: %(pager_size)s;
    padding: %(space_0)s;
}
QPushButton#PagerButton:hover {
    background: %(surface_hover)s;
    border-color: %(primary)s;
    color: %(text_primary)s;
}
QPushButton#PagerButton:pressed {
    background: %(surface_active)s;
}
QPushButton#PagerButton:disabled {
    background: %(surface_muted)s;
    border-color: %(border_muted)s;
    color: %(text_disabled)s;
}
QHeaderView::section:last {
    border-right: 0;
}
QTableCornerButton::section {
    background: %(surface)s;
    border: 0;
}
QScrollBar:vertical, QScrollBar:horizontal {
    background: %(bg)s;
    border: 0;
    margin: %(space_0)s;
}
QScrollBar:vertical {
    width: %(space_3)s;
}
QScrollBar:horizontal {
    height: %(space_3)s;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background: %(border_strong)s;
    border-radius: %(radius_md)s;
    min-height: %(space_7)s;
    min-width: %(space_7)s;
}
QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
    background: %(border_strong)s;
}
QScrollBar::handle:vertical:pressed, QScrollBar::handle:horizontal:pressed {
    background: %(primary)s;
}
QScrollBar::add-line, QScrollBar::sub-line {
    height: %(space_0)s;
    width: %(space_0)s;
}
QMenu {
    background: %(surface)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_md)s;
    color: %(text_primary)s;
    padding: %(space_1)s;
}
QMenu::item {
    border-radius: %(radius_sm)s;
    padding: %(space_2)s %(space_5)s;
}
QMenu::item:selected {
    background: %(selection)s;
}
QMenu::item:disabled {
    color: %(text_disabled)s;
}
QMessageBox, QInputDialog, QProgressDialog {
    background: %(bg)s;
    color: %(text_primary)s;
}
QMessageBox QLabel {
    background: transparent;
    color: %(text_primary)s;
}
QMessageBox QPushButton, QDialogButtonBox QPushButton {
    min-width: %(button_min_width)s;
}
QProgressBar {
    background: %(surface_alt)s;
    border: 1px solid %(border)s;
    border-radius: %(radius_md)s;
    color: %(text_primary)s;
    text-align: center;
}
QProgressBar::chunk {
    background: %(primary)s;
    border-radius: %(radius_sm)s;
}
QToolTip {
    background: %(surface)s;
    border: 1px solid %(border_strong)s;
    border-radius: %(radius_sm)s;
    color: %(text_primary)s;
    padding: %(space_1)s %(space_2)s;
}
"""
