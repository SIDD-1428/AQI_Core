function NavItem({
  item,
  expanded,
  activePage,
  onSelectPage,
}) {
  const Icon = item.icon;

  const active = item.id === activePage;

  return (
    <button
      className={`nav-item ${
        active ? "nav-item-active" : ""
      }`}
      onClick={() => onSelectPage(item.id)}
    >
      <Icon
        size={19}
        strokeWidth={1.6}
        className="nav-icon"
      />

      {expanded && (
        <span className="nav-label">
          {item.title}
        </span>
      )}
    </button>
  );
}

export default NavItem;