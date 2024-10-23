import NavTooltip from "./NavTooltip";
import { AnimatedButton } from "./AnimatedButton";
import Link from "next/link";
import Logo from "./Logo";

const pages = [
  {
    name: "Targets",
    link: "/targets",
    enabled: true,
  },
  {
    name: "Observations",
    link: "/observations",
    enabled: true,
  },
  {
    name: "Data Products",
    link: "/data-products",
    enabled: true,
  },
  {
    name: "Annoucements",
    link: "/announcements",
    enabled: true,
  },
  {
    name: "About us",
    link: "/about",
    enabled: true,
  },
];

function NavBar() {
  return (
    <div className="w-full min-w-0 h-16 px-2 sm:px-6 lg:px-8 static flex items-center justify-around backdrop-blur-sm">
      <Logo />
      <div>
        <nav className="flex">
          {pages.map((page) => (
            <AnimatedButton
              key={page.name}
              href={page.link}
              disabled={!page.enabled}
            >
              {page.name}
            </AnimatedButton>
          ))}
        </nav>
      </div>
      <div>
        <NavTooltip />
      </div>
    </div>
  );
}

export { NavBar };
